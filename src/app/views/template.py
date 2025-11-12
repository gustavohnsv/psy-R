from docx import Document
from docx.opc.exceptions import OpcError
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Signal

from .ui_template import Ui_TelaTemplate

class TemplateScreen(QWidget):
    avancar_clicado = Signal()
    carregar_template_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_template = None
        self.ui = Ui_TelaTemplate()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self._tentar_avancar)
        self._template_carregado = False

        self.configurar_botao_carregar()

    def configurar_botao_carregar(self):
        botao_carregar = self.ui.btn_carregar
        botao_carregar.clicked.connect(self.carregar_template)

    def carregar_template(self):
        file_path, _ = QFileDialog.getOpenFileName(self)
        if file_path:
            try:
                self.file_template = Document(file_path)
                self.ui.lineEdit_caminho_template.setText(file_path)
                
                # Só permite avançar após carregar o template
                self._template_carregado = True
                print(f'Template {file_path} carregado com sucesso')
            except OpcError as e:
                print(f'Erro: O arquivo {file_path} não é um documento .docx válido!')
                self.file_template = None
            except Exception as e:
                print(f'Erro inesperado ao carregar o arquivo: {e}')
                self.file_template = None


    def debug(self):
        print("Funcionando!")

    def _tentar_avancar(self):
        if self._template_carregado:
            self.avancar_clicado.emit()
        else:
            QMessageBox.warning(
                self,
                'Atenção',
                'É necessário carregar um template antes de avançar!'
            )
    
    def get_template_path(self) -> str:
        """Get the template file path."""
        return self.ui.lineEdit_caminho_template.text() if self._template_carregado else ""
    
    def get_template_document(self) -> Document:
        """Get the loaded template document."""
        return self.file_template