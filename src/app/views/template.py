from docx import Document
from docx.opc.exceptions import OpcError
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Signal

from .ui_template import Ui_TelaTemplate

class TemplateScreen(QWidget):
    next_clicked = Signal()
    load_template_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_template = None
        self.ui = Ui_TelaTemplate()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self._try_advance)
        self._template_loaded = False

        self.setup_load_button()

    def setup_load_button(self):
        load_button = self.ui.btn_carregar
        load_button.clicked.connect(self.load_template)

    def load_template(self):
        import os
        from app.utils.paths import get_app_dir
        
        # Templates folder relative to the executable (or project root in dev)
        templates_dir = get_app_dir() / "templates"
        
        if not templates_dir.exists():
             # Try to find it in data/templates as fallback (dev mode structure sometimes)
             # But get_app_dir() in dev points to project root, so templates should be at root/templates?
             # Actually, in dev, the user might have them in src/app/data/templates.
             # Let's check both or just rely on get_app_dir() logic.
             # In dev: get_app_dir() -> project root.
             # If user keeps templates in project_root/templates, it works.
             # If they are in src/app/data/templates, we might need a fallback or move them.
             # Given the user wants "same folder as the app", let's stick to that.
             # But for dev convenience, let's also check the source location.
             dev_templates = get_app_dir() / "src" / "app" / "data" / "templates"
             if dev_templates.exists():
                 templates_dir = dev_templates
        
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Template", str(templates_dir), "Word Documents (*.docx)")
        if file_path:
            try:
                self.file_template = Document(file_path)
                self.ui.lineEdit_caminho_template.setText(file_path)
                
                # Only allow advancing after loading the template
                self._template_loaded = True
                print(f'Template {file_path} loaded successfully')
            except OpcError as e:
                print(f'Error: File {file_path} is not a valid .docx document!')
                self.file_template = None
            except Exception as e:
                print(f'Unexpected error loading file: {e}')
                self.file_template = None


    def debug(self):
        print("Working!")

    def _try_advance(self):
        if self._template_loaded:
            self.next_clicked.emit()
        else:
            QMessageBox.warning(
                self,
                'Attention',
                'You must load a template before advancing!'
            )
    
    def get_template_path(self) -> str:
        """Get the template file path."""
        return self.ui.lineEdit_caminho_template.text() if self._template_loaded else ""
    
    def get_template_document(self) -> Document:
        """Get the loaded template document."""
        return self.file_template