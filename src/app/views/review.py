from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from typing import Optional

from .ui_review import Ui_TelaRevisao

class ReviewScreen(QWidget):
    voltar_clicado = Signal()
    gerar_laudo_clicado = Signal()

    def __init__(self, parent=None, data_model=None):
        super().__init__(parent)
        self.ui = Ui_TelaRevisao()
        self.ui.setupUi(self)
        self.data_model = data_model

        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)
        self.ui.btn_gerar_laudo.clicked.connect(self.gerar_laudo_clicado.emit)
    
    def set_data_model(self, data_model):
        """Set the data model for this screen."""
        self.data_model = data_model
    
    def showEvent(self, event):
        """Override showEvent to populate summary when screen is shown."""
        super().showEvent(event)
        self.populate_summary()
    
    def populate_summary(self):
        """Populate the review screen with collected data summary."""
        if not self.data_model:
            self.ui.label_revisao.setText("Nenhum dado disponível para revisão.")
            return
        
        summary_lines = []
        summary_lines.append("<h2>Resumo dos Dados Coletados</h2>")
        summary_lines.append("<hr>")
        
        # Template information
        if self.data_model.template_path:
            summary_lines.append(f"<b>Template:</b> {self.data_model.template_path}")
        else:
            summary_lines.append("<b>Template:</b> <span style='color: red;'>Não carregado</span>")
        
        summary_lines.append("<br>")
        
        # Patient data
        summary_lines.append("<h3>Dados do Paciente</h3>")
        patient = self.data_model.patient_data
        if patient.get("patient_name"):
            summary_lines.append(f"<b>Nome:</b> {patient.get('patient_name', 'N/A')}")
            summary_lines.append(f"<b>Data de Nascimento:</b> {patient.get('patient_birth', 'N/A')}")
            summary_lines.append(f"<b>Idade Cronológica:</b> {patient.get('patient_crono_age', 'N/A')}")
            summary_lines.append(f"<b>Escola:</b> {patient.get('patient_school', 'N/A')}")
            summary_lines.append(f"<b>Turma:</b> {patient.get('patient_class', 'N/A')}")
        else:
            summary_lines.append("<span style='color: orange;'>Dados do paciente não preenchidos</span>")
        
        summary_lines.append("<br>")
        
        # Respondent 1 data
        summary_lines.append("<h3>1º Responsável</h3>")
        resp1 = self.data_model.resp1_data
        if resp1.get("resp1_name"):
            summary_lines.append(f"<b>Nome:</b> {resp1.get('resp1_name', 'N/A')}")
            summary_lines.append(f"<b>Profissão:</b> {resp1.get('resp1_career', 'N/A')}")
            summary_lines.append(f"<b>Escolaridade:</b> {resp1.get('resp1_education', 'N/A')}")
            summary_lines.append(f"<b>Idade:</b> {resp1.get('resp1_age', 'N/A')}")
        else:
            summary_lines.append("<span style='color: orange;'>Dados do 1º responsável não preenchidos</span>")
        
        summary_lines.append("<br>")
        
        # Respondent 2 data
        summary_lines.append("<h3>2º Responsável</h3>")
        resp2 = self.data_model.resp2_data
        if resp2.get("resp2_name"):
            summary_lines.append(f"<b>Nome:</b> {resp2.get('resp2_name', 'N/A')}")
            summary_lines.append(f"<b>Profissão:</b> {resp2.get('resp2_career', 'N/A')}")
            summary_lines.append(f"<b>Escolaridade:</b> {resp2.get('resp2_education', 'N/A')}")
            summary_lines.append(f"<b>Idade:</b> {resp2.get('resp2_age', 'N/A')}")
        else:
            summary_lines.append("<span style='color: orange;'>Dados do 2º responsável não preenchidos</span>")
        
        summary_lines.append("<br>")
        
        # Test results
        summary_lines.append("<h3>Resultados dos Testes</h3>")
        if self.data_model.test_results:
            for test_name, test_data in self.data_model.test_results.items():
                summary_lines.append(f"<b>{test_name}:</b> {test_data}")
        else:
            summary_lines.append("<span style='color: orange;'>Nenhum resultado de teste registrado</span>")
        
        summary_lines.append("<br>")
        
        # Conclusion
        summary_lines.append("<h3>Conclusão</h3>")
        if self.data_model.conclusion_text:
            conclusion_preview = self.data_model.conclusion_text[:200]
            if len(self.data_model.conclusion_text) > 200:
                conclusion_preview += "..."
            summary_lines.append(f"{conclusion_preview}")
        else:
            summary_lines.append("<span style='color: orange;'>Conclusão não preenchida</span>")
        
        summary_lines.append("<br>")
        summary_lines.append("<hr>")
        
        # Field mapping preview
        summary_lines.append("<h3>Mapeamento de Campos</h3>")
        field_mapping = self.data_model.get_field_mapping()
        if field_mapping:
            summary_lines.append("<table border='1' cellpadding='5' style='border-collapse: collapse;'>")
            summary_lines.append("<tr><th>Campo do Template</th><th>Valor</th></tr>")
            for field, value in sorted(field_mapping.items()):
                display_value = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                if not value or str(value).strip() == "":
                    display_value = "<span style='color: red;'>VAZIO</span>"
                summary_lines.append(f"<tr><td>{{{field}}}</td><td>{display_value}</td></tr>")
            summary_lines.append("</table>")
        else:
            summary_lines.append("<span style='color: orange;'>Nenhum campo mapeado</span>")
        
        summary_text = "<br>".join(summary_lines)
        self.ui.label_revisao.setText(summary_text)