from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QScrollArea
from PySide6.QtCore import Signal, Qt

from app.services.review_service import ReviewService

class ReviewScreen(QWidget):
    """Screen for reviewing collected data before report generation."""
    
    back_clicked = Signal()
    generate_report_clicked = Signal()

    def __init__(self, data_model=None):
        super().__init__()
        self._data_model = data_model
        self._review_service = ReviewService()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Title
        lbl_title = QLabel("Revisão e Geração do Laudo")
        lbl_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        lbl_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_title)

        # Scroll Area for content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        self.lbl_summary = QLabel("Aqui serão exibidos todos os dados inseridos para a conferência final...")
        self.lbl_summary.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lbl_summary.setWordWrap(True)
        self.lbl_summary.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        scroll_layout.addWidget(self.lbl_summary)
        scroll_area.setWidget(scroll_content)
        
        layout.addWidget(scroll_area)

        # Buttons
        btn_layout = QHBoxLayout()
        
        self.btn_back = QPushButton("Voltar")
        self.btn_back.clicked.connect(self.back_clicked.emit)
        btn_layout.addWidget(self.btn_back)
        
        btn_layout.addStretch()
        
        self.btn_generate_report = QPushButton("Confirmar e Gerar Laudo")
        self.btn_generate_report.setStyleSheet("font-weight: bold;")
        self.btn_generate_report.clicked.connect(self.generate_report_clicked.emit)
        btn_layout.addWidget(self.btn_generate_report)

        layout.addLayout(btn_layout)
    
    def set_data_model(self, data_model):
        """Set the data model for this screen."""
        self._data_model = data_model
    
    def showEvent(self, event):
        """Override showEvent to populate summary when screen is shown."""
        super().showEvent(event)
        self.populate_summary()
    
    def populate_summary(self):
        """Populate the review screen with collected data summary."""
        if not self._data_model:
            self.lbl_summary.setText("Nenhum dado disponível para revisão.")
            return
        
        summary_html = self._review_service.generate_html_summary(self._data_model)
        self.lbl_summary.setText(summary_html)