from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal

from app.services.report_summary_service import ReportSummaryService

class ConclusionScreen(QWidget):
    """Screen for displaying and editing the conclusion summary."""
    
    next_clicked = Signal()
    back_clicked = Signal()

    def __init__(self, data_model=None):
        super().__init__()
        self._data_model = data_model
        self._summary_service = ReportSummaryService()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Title
        lbl_title = QLabel("Conclusão e Síntese")
        lbl_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(lbl_title)

        # Instruction
        lbl_instruction = QLabel("Abaixo está uma sugestão de síntese baseada nos resultados. Edite conforme necessário.")
        layout.addWidget(lbl_instruction)

        # Text area
        self.txt_conclusao = QTextEdit()
        layout.addWidget(self.txt_conclusao)

        # Buttons
        btn_layout = QHBoxLayout()
        
        self.btn_voltar = QPushButton("Voltar")
        self.btn_voltar.clicked.connect(self.back_clicked.emit)
        btn_layout.addWidget(self.btn_voltar)
        
        btn_layout.addStretch()
        
        self.btn_avancar = QPushButton("Avançar para Revisão")
        self.btn_avancar.clicked.connect(self.next_clicked.emit)
        btn_layout.addWidget(self.btn_avancar)

        layout.addLayout(btn_layout)

    def refresh_calculated_data(self):
        """Refresh the summary text based on current test results."""
        if not self._data_model:
            return
            
        # Only update if text is empty to avoid overwriting user edits
        # Or if we want to force update (could add a "Regenerate" button later)
        if not self.txt_conclusao.toPlainText().strip():
            summary = self._summary_service.build_summary_text(self._data_model.test_results)
            self.txt_conclusao.setPlainText(summary)

    def get_data(self):
        """Return the current text."""
        return {
            "conclusion_text": self.txt_conclusao.toPlainText()
        }