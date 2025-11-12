from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .ui_conclusion import Ui_TelaConclusao

class ConclusionScreen(QWidget):
    avancar_clicado = Signal()
    voltar_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaConclusao()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)
        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)
    
    def get_data(self):
        """Get conclusion text data."""
        return {
            "conclusao_text": self.ui.textEdit_conclusao.toPlainText()
        }