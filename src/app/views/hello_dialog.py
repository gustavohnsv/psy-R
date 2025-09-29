from PySide6.QtWidgets import QDialog

from .ui_hello_dialog import Ui_Dialog # Importa o design gerado

class HelloDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) # Configura o design