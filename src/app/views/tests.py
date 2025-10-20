from functools import partial
from PySide6.QtWidgets import QWidget, QPushButton, QStackedWidget
from PySide6.QtCore import Signal

from .ui_tests import Ui_TelaTestes

class TestsScreen(QWidget):
    avancar_clicado = Signal()
    voltar_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaTestes()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)
        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)

        self.configurar_botoes_teste()

    def configurar_botoes_teste(self):
        stacked_forms = self.ui.stackedWidget_formularios

        botoes_testes = [
            self.ui.btn_teste1, self.ui.btn_teste2, self.ui.btn_teste3,
            self.ui.btn_teste4, self.ui.btn_teste5, self.ui.btn_teste6,
            self.ui.btn_teste7, self.ui.btn_teste8, self.ui.btn_teste9,
        ]

        for i, btn in enumerate(botoes_testes):
            # O índice 0 é a página "Selecione...", então o botão 1 (i=0) vai para a página 1
            btn.clicked.connect(partial(self.mostrar_form_teste, stacked_forms, i + 1))

    def mostrar_form_teste(self, stacked_widget, index):
        if index < stacked_widget.count():
            stacked_widget.setCurrentIndex(index)
        else:
            print(f"Aviso: Formulário de teste (índice {index}) não encontrado.")