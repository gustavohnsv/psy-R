from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal, Qt

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
        main_layout = QVBoxLayout(self)

        # Title
        lbl_title = QLabel("Conclusão")
        lbl_title.setStyleSheet("font-size: 18px; font-weight: bold; alignment: center;")
        lbl_title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(lbl_title)

        # Content Layout (Split View)
        content_layout = QHBoxLayout()

        # Left Side: Calculated Data (Read-only)
        left_layout = QVBoxLayout()
        lbl_left = QLabel("Dados Calculados para Referência")
        lbl_left.setStyleSheet("font-weight: bold;")
        left_layout.addWidget(lbl_left)

        self.txt_calculated_data = QTextEdit()
        self.txt_calculated_data.setReadOnly(True)
        self.txt_calculated_data.setStyleSheet("background-color: #f0f0f0;")
        left_layout.addWidget(self.txt_calculated_data)
        
        content_layout.addLayout(left_layout)

        # Right Side: Conclusion Text (Editable)
        right_layout = QVBoxLayout()
        lbl_right = QLabel("Conclusão e Parecer Psicológico")
        lbl_right.setStyleSheet("font-weight: bold;")
        right_layout.addWidget(lbl_right)

        self.txt_conclusao = QTextEdit()
        right_layout.addWidget(self.txt_conclusao)

        content_layout.addLayout(right_layout)
        
        main_layout.addLayout(content_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        
        self.btn_voltar = QPushButton("Voltar")
        self.btn_voltar.clicked.connect(self.back_clicked.emit)
        btn_layout.addWidget(self.btn_voltar)
        
        btn_layout.addStretch()
        
        self.btn_avancar = QPushButton("Avançar para Revisão")
        self.btn_avancar.clicked.connect(self.next_clicked.emit)
        btn_layout.addWidget(self.btn_avancar)

        main_layout.addLayout(btn_layout)

    def refresh_calculated_data(self):
        """Refresh the summary text based on current test results."""
        if not self._data_model:
            return
            
        # Update the left side with the calculated summary
        summary = self._summary_service.build_summary_text(self._data_model.test_results)
        self.txt_calculated_data.setPlainText(summary)
        
        # Pre-fill the right side ONLY if it's empty (optional, maybe user wants to start fresh or copy-paste)
        # For now, let's leave it empty or maybe just put a placeholder if needed.
        # The user request says "let the user write freely", so maybe we don't auto-fill the right side 
        # with the summary anymore, or maybe we do but allow editing.
        # Given the image shows the left side populated and right side empty-ish, 
        # I'll assume the left is for reference and right is for writing.
        # If the user wants to copy from left to right, they can.
        
        # However, if the model already has a conclusion text (e.g. from previous navigation), restore it.
        current_conclusion = self._data_model.conclusion_text
        if current_conclusion:
             self.txt_conclusao.setPlainText(current_conclusion)

    def get_data(self):
        """Return the current text."""
        return {
            "conclusion_text": self.txt_conclusao.toPlainText()
        }