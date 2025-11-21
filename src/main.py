import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QFileDialog, QMessageBox
from docx import Document

from app.views import (
    TemplateScreen,
    PatientScreen,
    TemplateFieldsScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen,
)
from app.models import ReportDataModel
from app.controllers.navigation_controller import NavigationController
from app.controllers.main_controller import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiqueLaudo")
        self.resize(800, 600)

        # Initialize data model
        self.data_model = ReportDataModel()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize controllers
        self.main_controller = MainController(self, self.data_model)
        self.nav_controller = NavigationController(self.stacked_widget)

        self.create_and_connect_screens()
        self.stacked_widget.setCurrentIndex(0)

    def create_and_connect_screens(self):

        self.template_screen = TemplateScreen()
        self.patient_screen = PatientScreen()
        # Split template fields into focused screens (administrative, clinical, behavior, conclusions)
        self.admin_fields_screen = TemplateFieldsScreen()
        self.admin_fields_screen.set_sections(["administrativo"])

        self.clinical_context_screen = TemplateFieldsScreen()
        self.clinical_context_screen.set_sections(["contexto_clinico"])

        self.behavior_screen = TemplateFieldsScreen()
        self.behavior_screen.set_sections(["comportamento_observado"])
        # Conclusions use the same dynamic screen but restricted to the conclusions section
        self.conclusions_section_screen = TemplateFieldsScreen()
        self.conclusions_section_screen.set_sections(["conclusoes"])

        # Keep a backward-compatible separate ConclusionScreen instance (some tests / callers expect it)
        self.conclusion_screen = ConclusionScreen(data_model=self.data_model)

        self.tests_screen = TestsScreen()
        self.review_screen = ReviewScreen(data_model=self.data_model)

        # Order: template -> patient -> admin fields -> clinical -> behavior -> tests -> conclusions -> review
        self.stacked_widget.addWidget(self.template_screen)
        self.stacked_widget.addWidget(self.patient_screen)
        self.stacked_widget.addWidget(self.admin_fields_screen)
        self.stacked_widget.addWidget(self.clinical_context_screen)
        self.stacked_widget.addWidget(self.behavior_screen)
        self.stacked_widget.addWidget(self.tests_screen)
        # add both conclusions widgets (conclusions section and legacy conclusion screen) to preserve API/indices
        self.stacked_widget.addWidget(self.conclusions_section_screen)
        self.stacked_widget.addWidget(self.conclusion_screen)
        self.stacked_widget.addWidget(self.review_screen)
        
        # Register navigation callbacks
        # Before leaving any screen, collect data
        for i in range(self.stacked_widget.count()):
            self.nav_controller.register_before_navigation(i, self.main_controller.collect_data_from_current_view)
            self.nav_controller.register_after_navigation(i, lambda idx=i: self.main_controller.prepare_view(idx))

        # Connect signals
        self.template_screen.next_clicked.connect(self.nav_controller.next_screen)

        self.patient_screen.next_clicked.connect(self.nav_controller.next_screen)
        self.patient_screen.back_clicked.connect(self.nav_controller.previous_screen)

        for tela in (self.admin_fields_screen, self.clinical_context_screen, self.behavior_screen, self.conclusions_section_screen):
            tela.next_clicked.connect(self.nav_controller.next_screen)
            tela.back_clicked.connect(self.nav_controller.previous_screen)

        self.tests_screen.next_clicked.connect(self.nav_controller.next_screen)
        self.tests_screen.back_clicked.connect(self.nav_controller.previous_screen)

        # conclusions section leads to review
        # We need a special handler for this to jump to review screen
        self.conclusions_section_screen.next_clicked.connect(lambda: self.nav_controller.go_to_screen(self.review_screen))
        self.conclusions_section_screen.back_clicked.connect(self.nav_controller.previous_screen)

        # wire legacy conclusion screen as before (backward compatibility)
        self.conclusion_screen.next_clicked.connect(lambda: self.nav_controller.go_to_screen(self.review_screen))
        self.conclusion_screen.back_clicked.connect(self.nav_controller.previous_screen)

        self.review_screen.back_clicked.connect(self.nav_controller.previous_screen)
        self.review_screen.generate_report_clicked.connect(self.main_controller.generate_report)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())