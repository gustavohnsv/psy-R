from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .ui_patient import Ui_TelaPaciente

class PatientScreen(QWidget):
    next_clicked = Signal()
    back_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaPaciente()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.next_clicked.emit)
        self.ui.btn_voltar.clicked.connect(self.back_clicked.emit)

        self.setup_data_capture()
        # Hide chronological age field from the UI (calculated automatically in the data model)
        try:
            self.ui.label_idade_crono.hide()
            self.ui.lineEdit_idade_crono.hide()
        except Exception:
            # If the UI was regenerated with different names, fail silently
            pass

    def setup_data_capture(self):
        next_button = self.ui.btn_avancar
        next_button.clicked.connect(self.capture_data)

    def capture_data(self):
        """Legacy method - kept for backward compatibility."""
        data = self.get_data()
        for item in [data.get("patient", {}), data.get("resp1", {}), data.get("resp2", {})]:
            if item:
                print(item)
    
    def get_data(self):
        """Get all patient and respondent data as a structured dictionary."""
        # helper to compute age from QDate text
        def _compute_crono_age_from_date_text(date_text: str) -> str:
            if not date_text:
                return ""
            try:
                from datetime import datetime, date
                parsed = datetime.strptime(date_text, "%d/%m/%Y").date()
                today = date.today()
                years = today.year - parsed.year - ((today.month, today.day) < (parsed.month, parsed.day))
                return str(years)
            except Exception:
                return ""
        patient_data = {
            "patient_name": self.ui.lineEdit_nome.text(),
            "patient_birth": self.ui.dateEdit_nascimento.text(),
            # Provide `patient_crono_age` for compatibility: compute from the date edit if possible.
            # Prefer explicit value if present (keeps compatibility with tests and hidden field usage)
            "patient_crono_age": (self.ui.lineEdit_idade_crono.text() if getattr(self.ui, "lineEdit_idade_crono", None) and self.ui.lineEdit_idade_crono.text() else _compute_crono_age_from_date_text(self.ui.dateEdit_nascimento.text())),
            "patient_school": self.ui.lineEdit_escola.text(),
            "patient_class": self.ui.lineEdit_turma.text()
        }

        resp1_idade = self.ui.lineEdit_resp1_idade.text()
        try:
            resp1_idade_int = int(resp1_idade)
        except (ValueError, TypeError):
            resp1_idade_int = 0

        resp1_data = {
            "resp1_name": self.ui.lineEdit_resp1_nome.text(),
            "resp1_career": self.ui.lineEdit_resp1_profissao.text(),
            "resp1_education": self.ui.lineEdit_resp1_escolaridade.text(),
            "resp1_age": resp1_idade_int
        }

        resp2_idade = self.ui.lineEdit_resp2_idade.text()
        try:
            resp2_idade_int = int(resp2_idade)
        except (ValueError, TypeError):
            resp2_idade_int = 0

        resp2_data = {
            "resp2_name": self.ui.lineEdit_resp2_nome.text(),
            "resp2_career": self.ui.lineEdit_resp2_profissao.text(),
            "resp2_education": self.ui.lineEdit_resp2_escolaridade.text(),
            "resp2_age": resp2_idade_int
        }

        return {
            "patient": patient_data,
            "resp1": resp1_data,
            "resp2": resp2_data,
            "template_fields": {
                "solicitante_nome": self.ui.lineEdit_solicitante_nome.text(),
                "solicitante_crp": self.ui.lineEdit_solicitante_crp.text()
            }
        }