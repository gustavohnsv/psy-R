import sys
from PySide6.QtWidgets import QApplication
from app.views import WizardMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cria e exibe a janela do wizard
    window = WizardMainWindow()
    window.show()

    # Inicia o loop da aplicação
    sys.exit(app.exec())