from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .ui_review import Ui_TelaRevisao

class ReviewScreen(QWidget):
    voltar_clicado = Signal()
    gerar_laudo_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaRevisao()
        self.ui.setupUi(self)

        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)
        self.ui.btn_gerar_laudo.clicked.connect(self.gerar_laudo_clicado.emit)