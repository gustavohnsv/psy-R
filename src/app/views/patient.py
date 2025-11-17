from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .ui_patient import Ui_TelaPaciente

class PatientScreen(QWidget):
    avancar_clicado = Signal()
    voltar_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaPaciente()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)
        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)

        self.configurar_capturar_dados()

    def configurar_capturar_dados(self):
        botao_avancar = self.ui.btn_avancar
        botao_avancar.clicked.connect(self.capturar_dados)

    def capturar_dados(self):
        """Legacy method - kept for backward compatibility."""
        data = self.get_data()
        for item in [data.get("patient", {}), data.get("resp1", {}), data.get("resp2", {})]:
            if item:
                print(item)
    
    def get_data(self):
        """Get all patient and respondent data as a structured dictionary."""
        patient_data = {
            "patient_name": self.ui.lineEdit_nome.text(),
            "patient_birth": self.ui.dateEdit_nascimento.text(),
            "patient_crono_age": self.ui.lineEdit_idade_crono.text(),
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