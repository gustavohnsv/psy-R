"""Unit tests for MainController."""
import pytest
from unittest.mock import Mock, MagicMock, patch
from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow

from app.controllers.main_controller import MainController
from app.models.data_model import ReportDataModel
from app.views import (
    TemplateScreen,
    PatientScreen,
    TemplateFieldsScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen,
)

@pytest.fixture
def mock_main_window():
    window = Mock(spec=QMainWindow)
    window.stacked_widget = Mock(spec=QStackedWidget)
    return window

@pytest.fixture
def mock_data_model():
    return Mock(spec=ReportDataModel)

@pytest.fixture
def controller(mock_main_window, mock_data_model):
    return MainController(mock_main_window, mock_data_model)

class TestMainControllerDataCollection:
    """Test data collection logic in MainController."""
    
    def test_collect_template_data(self, controller):
        """Test collecting data from TemplateScreen."""
        widget = Mock(spec=TemplateScreen)
        widget.get_template_path.return_value = "/path/to/template.docx"
        widget.get_template_document.return_value = Mock()
        
        controller.main_window.stacked_widget.currentWidget.return_value = widget
        
        controller.collect_data_from_current_view()
        
        controller.data_model.set_template.assert_called_once()
        
    def test_collect_patient_data(self, controller):
        """Test collecting data from PatientScreen."""
        widget = Mock(spec=PatientScreen)
        widget.get_data.return_value = {
            "patient": {"name": "John"},
            "resp1": {"name": "Mary"},
            "resp2": {"name": "Joe"},
            "template_fields": {"field": "value"}
        }
        
        controller.main_window.stacked_widget.currentWidget.return_value = widget
        
        controller.collect_data_from_current_view()
        
        controller.data_model.set_patient_data.assert_called_with({"name": "John"})
        controller.data_model.set_resp1_data.assert_called_with({"name": "Mary"})
        controller.data_model.set_resp2_data.assert_called_with({"name": "Joe"})
        controller.data_model.set_template_field_values.assert_called_with({"field": "value"})
        
    def test_collect_template_fields_data(self, controller):
        """Test collecting data from TemplateFieldsScreen."""
        widget = Mock(spec=TemplateFieldsScreen)
        widget.get_data.return_value = {
            "field1": "value1",
            "CONCLUSAO_ANALISE_LIVRE": "Conclusion Text"
        }
        
        controller.main_window.stacked_widget.currentWidget.return_value = widget
        
        controller.collect_data_from_current_view()
        
        controller.data_model.set_template_field_values.assert_called()
        controller.data_model.set_conclusion_text.assert_called_with("Conclusion Text")
        
    def test_collect_tests_data(self, controller):
        """Test collecting data from TestsScreen."""
        widget = Mock(spec=TestsScreen)
        widget.get_data.return_value = {"test1": 10}
        
        controller.main_window.stacked_widget.currentWidget.return_value = widget
        # Mock existence of conclusion_screen
        controller.main_window.conclusion_screen = Mock()
        
        controller.collect_data_from_current_view()
        
        controller.data_model.set_test_results.assert_called_with({"test1": 10})
        controller.main_window.conclusion_screen.refresh_calculated_data.assert_called_once()
        
    def test_collect_conclusion_data(self, controller):
        """Test collecting data from ConclusionScreen."""
        widget = Mock(spec=ConclusionScreen)
        widget.get_data.return_value = {"conclusion_text": "Final Conclusion"}
        
        controller.main_window.stacked_widget.currentWidget.return_value = widget
        
        controller.collect_data_from_current_view()
        
        controller.data_model.set_conclusion_text.assert_called_with("Final Conclusion")

class TestMainControllerViewPreparation:
    """Test view preparation logic in MainController."""
    
    def test_prepare_template_fields_screen(self, controller):
        """Test preparing TemplateFieldsScreen."""
        widget = Mock(spec=TemplateFieldsScreen)
        controller.main_window.stacked_widget.widget.return_value = widget
        controller.data_model.get_template_field_values.return_value = {"field": "value"}
        
        controller.prepare_view(1)
        
        widget.set_data.assert_called_with({"field": "value"})
        
    def test_prepare_conclusion_screen(self, controller):
        """Test preparing ConclusionScreen."""
        widget = Mock(spec=ConclusionScreen)
        controller.main_window.stacked_widget.widget.return_value = widget
        
        controller.prepare_view(2)
        
        widget.refresh_calculated_data.assert_called_once()

class TestMainControllerReportGeneration:
    """Test report generation logic in MainController."""
    
    @patch('app.controllers.main_controller.TemplateProcessor')
    @patch('app.controllers.main_controller.QMessageBox')
    @patch('app.controllers.main_controller.QFileDialog')
    @patch('docx.Document')
    def test_generate_report_success(self, mock_document, mock_filedialog, mock_messagebox, mock_processor_class, controller):
        """Test successful report generation."""
        # Setup
        controller.data_model.is_template_loaded.return_value = True
        controller.data_model.template_path = "/path/to/template.docx"
        controller.data_model.template_document = Mock()
        controller.data_model.get_field_mapping.return_value = {"field": "value"}
        controller.data_model.patient_data = {"patient_name": "John Doe"}
        
        mock_processor = mock_processor_class.return_value
        mock_processor.validate_fields.return_value = ([], [])
        mock_processor.check_required_fields.return_value = ([], [])
        
        mock_filedialog.getExistingDirectory.return_value = "/output/dir"
        
        # Execute
        controller.generate_report()
        
        # Verify
        mock_processor.replace_fields.assert_called()
        mock_processor.save_document.assert_called()
        mock_messagebox.information.assert_called()
        
    @patch('app.controllers.main_controller.QMessageBox')
    def test_generate_report_no_template(self, mock_messagebox, controller):
        """Test report generation fails if no template loaded."""
        controller.data_model.is_template_loaded.return_value = False
        
        controller.generate_report()
        
        mock_messagebox.critical.assert_called()
