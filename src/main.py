import sys
from PySide6.QtWidgets import QApplication
from app.views import MainWindow # Importação limpa graças ao __init__.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria e exibe a janela principal
    window = MainWindow()
    window.show()
    
    # Inicia o loop da aplicação
    sys.exit(app.exec())