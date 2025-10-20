from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .ui_template import Ui_TelaTemplate

class TemplateScreen(QWidget):
    avancar_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaTemplate()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)