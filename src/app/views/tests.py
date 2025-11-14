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
            self.ui.btn_wisc4, self.ui.btn_ravlt, self.ui.btn_bpa2,
            self.ui.btn_neupsilin, self.ui.btn_srs2, self.ui.btn_etdah,
            self.ui.btn_cars2, self.ui.btn_htp, self.ui.btn_fdt,
        ]

        for i, btn in enumerate(botoes_testes):
            # O índice 0 é a página "Selecione...", então o botão 1 (i=0) vai para a página 1
            btn.clicked.connect(partial(self.mostrar_form_teste, stacked_forms, i + 1))

    def mostrar_form_teste(self, stacked_widget, index):
        if index < stacked_widget.count():
            stacked_widget.setCurrentIndex(index)
        else:
            print(f"Aviso: Formulário de teste (índice {index}) não encontrado.")
    
    def get_data(self):
        """Get test results data as a dictionary.
        
        Returns an empty dict for now - test result collection will be
        implemented when test forms are fully developed.
        """
        # TODO: Implement test result collection from UI forms
        return {}