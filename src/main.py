import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.views import (
    TemplateScreen,
    PatientScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente de Laudo Psicológico")
        self.resize(800, 600)

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
        index_atual = self.stacked_widget.currentIndex()
        if index_atual < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index_atual + 1)

    def ir_para_tela_anterior(self):
        index_atual = self.stacked_widget.currentIndex()
        if index_atual > 0:
            self.stacked_widget.setCurrentIndex(index_atual - 1)
    
    def gerar_laudo(self):
        print("Lógica para GERAR LAUDO executada!")
        # (Aqui você poderá coletar os dados de cada tela, ex: self.tela_paciente.get_data())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())