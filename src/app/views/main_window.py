from PySide6.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow # Importa o design da janela principal
from .hello_dialog import HelloDialog # Importa a classe do nosso diálogo

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Aplicação Principal")

        # Conecta o botão do nosso design a uma função
        self.hello_btn.clicked.connect(self.show_hello_dialog)

    def show_hello_dialog(self):
        print("Botão clicado, abrindo diálogo...")
        # Cria uma instância do nosso diálogo
        dialog = HelloDialog(self)
        
        # Define a mensagem no QLabel do diálogo
        dialog.message_label.setText("Olá, Mundo Estruturado!")
        
        # Executa o diálogo de forma modal
        dialog.exec()