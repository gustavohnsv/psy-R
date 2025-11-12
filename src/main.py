import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.views import (
    TemplateScreen,
    PatientScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen
)
from app.models import LaudoDataModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente de Laudo Psicológico")
        self.resize(800, 600)

        # Initialize data model
        self.data_model = LaudoDataModel()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.criar_e_conectar_telas()
        self.stacked_widget.setCurrentIndex(0)

    def criar_e_conectar_telas(self):

        self.tela_template = TemplateScreen()
        self.tela_paciente = PatientScreen()
        self.tela_testes = TestsScreen()
        self.tela_conclusao = ConclusionScreen()
        self.tela_revisao = ReviewScreen()

        self.stacked_widget.addWidget(self.tela_template)
        self.stacked_widget.addWidget(self.tela_paciente)
        self.stacked_widget.addWidget(self.tela_testes)
        self.stacked_widget.addWidget(self.tela_conclusao)
        self.stacked_widget.addWidget(self.tela_revisao)

        self.tela_template.avancar_clicado.connect(self.ir_para_proxima_tela)

        self.tela_paciente.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_paciente.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_testes.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_testes.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_conclusao.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_conclusao.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_revisao.voltar_clicado.connect(self.ir_para_tela_anterior)
        self.tela_revisao.gerar_laudo_clicado.connect(self.gerar_laudo)

    def ir_para_proxima_tela(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index_atual + 1)

    def ir_para_tela_anterior(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual > 0:
            self.stacked_widget.setCurrentIndex(index_atual - 1)
    
    def _coletar_dados_tela_atual(self):
        """Collect data from the currently visible screen."""
        index_atual = self.stacked_widget.currentIndex()
        
        # Screen 0: Template
        if index_atual == 0:
            template_path = self.tela_template.get_template_path()
            template_doc = self.tela_template.get_template_document()
            if template_path and template_doc:
                self.data_model.set_template(template_path, template_doc)
        
        # Screen 1: Patient
        elif index_atual == 1:
            patient_data = self.tela_paciente.get_data()
            if "patient" in patient_data:
                self.data_model.set_patient_data(patient_data["patient"])
            if "resp1" in patient_data:
                self.data_model.set_resp1_data(patient_data["resp1"])
            if "resp2" in patient_data:
                self.data_model.set_resp2_data(patient_data["resp2"])
        
        # Screen 2: Tests
        elif index_atual == 2:
            test_data = self.tela_testes.get_data()
            if test_data:
                self.data_model.set_test_results(test_data)
        
        # Screen 3: Conclusion
        elif index_atual == 3:
            conclusion_data = self.tela_conclusao.get_data()
            if "conclusao_text" in conclusion_data:
                self.data_model.set_conclusion_text(conclusion_data["conclusao_text"])
    
    def gerar_laudo(self):
        print("Lógica para GERAR LAUDO executada!")
        # (Aqui você poderá coletar os dados de cada tela, ex: self.tela_paciente.get_data())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())