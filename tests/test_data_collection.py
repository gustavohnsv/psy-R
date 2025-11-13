"""Unit tests for Branch 2: Data Collection Methods."""
import pytest
from unittest.mock import Mock, patch, MagicMock
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDate
import sys

# Ensure QApplication exists for GUI tests
if not QApplication.instance():
    app = QApplication(sys.argv)


@pytest.mark.unit
@pytest.mark.data_collection
class TestTemplateScreenDataCollection:
    """Test suite for TemplateScreen data collection methods."""
    
    def test_get_template_path_when_loaded(self):
        """Test getting template path when template is loaded."""
        from app.views.template import TemplateScreen
        
        screen = TemplateScreen()
        screen._template_carregado = True
        screen.ui.lineEdit_caminho_template.setText("/test/path/template.docx")
        
        path = screen.get_template_path()
        assert path == "/test/path/template.docx"
    
    def test_get_template_path_when_not_loaded(self):
        """Test getting template path when template is not loaded."""
        from app.views.template import TemplateScreen
        
        screen = TemplateScreen()
        screen._template_carregado = False
        
        path = screen.get_template_path()
        assert path == ""
    
    def test_get_template_document(self, sample_document):
        """Test getting template document."""
        from app.views.template import TemplateScreen
        
        screen = TemplateScreen()
        screen.file_template = sample_document
        
        doc = screen.get_template_document()
        assert doc == sample_document


@pytest.mark.unit
@pytest.mark.data_collection
class TestPatientScreenDataCollection:
    """Test suite for PatientScreen data collection methods."""
    
    def test_get_data_returns_structured_dict(self):
        """Test that get_data returns properly structured dictionary."""
        from app.views.patient import PatientScreen
        
        screen = PatientScreen()
        
        # Set some test data
        screen.ui.lineEdit_nome.setText("João Silva")
        screen.ui.dateEdit_nascimento.setDate(QDate(2010, 3, 15))
        screen.ui.lineEdit_idade_crono.setText("14")
        screen.ui.lineEdit_escola.setText("Escola Municipal")
        screen.ui.lineEdit_turma.setText("8º Ano")
        
        screen.ui.lineEdit_resp1_nome.setText("Maria Silva")
        screen.ui.lineEdit_resp1_profissao.setText("Professora")
        screen.ui.lineEdit_resp1_escolaridade.setText("Superior")
        screen.ui.lineEdit_resp1_idade.setText("35")
        
        screen.ui.lineEdit_resp2_nome.setText("José Silva")
        screen.ui.lineEdit_resp2_profissao.setText("Engenheiro")
        screen.ui.lineEdit_resp2_escolaridade.setText("Superior")
        screen.ui.lineEdit_resp2_idade.setText("38")
        
        data = screen.get_data()
        
        assert isinstance(data, dict)
        assert "patient" in data
        assert "resp1" in data
        assert "resp2" in data
        assert data["patient"]["patient_name"] == "João Silva"
        assert data["patient"]["patient_crono_age"] == "14"
        assert data["resp1"]["resp1_name"] == "Maria Silva"
        assert data["resp1"]["resp1_age"] == 35
        assert data["resp2"]["resp2_name"] == "José Silva"
        assert data["resp2"]["resp2_age"] == 38
    
    def test_get_data_handles_empty_fields(self):
        """Test that get_data handles empty fields correctly."""
        from app.views.patient import PatientScreen
        
        screen = PatientScreen()
        data = screen.get_data()
        
        assert data["patient"]["patient_name"] == ""
        assert data["resp1"]["resp1_age"] == 0
        assert data["resp2"]["resp2_age"] == 0
    
    def test_get_data_handles_invalid_age(self):
        """Test that get_data handles invalid age input."""
        from app.views.patient import PatientScreen
        
        screen = PatientScreen()
        screen.ui.lineEdit_resp1_idade.setText("invalid")
        screen.ui.lineEdit_resp2_idade.setText("abc")
        
        data = screen.get_data()
        
        assert data["resp1"]["resp1_age"] == 0
        assert data["resp2"]["resp2_age"] == 0


@pytest.mark.unit
@pytest.mark.data_collection
class TestTestsScreenDataCollection:
    """Test suite for TestsScreen data collection methods."""
    
    def test_get_data_returns_dict(self):
        """Test that get_data returns a dictionary."""
        from app.views.tests import TestsScreen
        
        screen = TestsScreen()
        data = screen.get_data()
        
        assert isinstance(data, dict)
        # Currently returns empty dict as test forms are not fully implemented
        assert data == {}


@pytest.mark.unit
@pytest.mark.data_collection
class TestConclusionScreenDataCollection:
    """Test suite for ConclusionScreen data collection methods."""
    
    def test_get_data_returns_conclusion_text(self):
        """Test that get_data returns conclusion text."""
        from app.views.conclusion import ConclusionScreen
        
        screen = ConclusionScreen()
        screen.ui.textEdit_conclusao.setPlainText("Test conclusion text")
        
        data = screen.get_data()
        
        assert isinstance(data, dict)
        assert "conclusao_text" in data
        assert data["conclusao_text"] == "Test conclusion text"
    
    def test_get_data_handles_empty_conclusion(self):
        """Test that get_data handles empty conclusion."""
        from app.views.conclusion import ConclusionScreen
        
        screen = ConclusionScreen()
        data = screen.get_data()
        
        assert data["conclusao_text"] == ""


@pytest.mark.integration
@pytest.mark.data_collection
class TestDataCollectionIntegration:
    """Integration tests for data collection across screens."""
    
    def test_mainwindow_collects_data_from_screens(self, qapp):
        """Test that MainWindow collects data from all screens."""
        from main import MainWindow
        from app.models import LaudoDataModel
        
        window = MainWindow()
        
        # Set up template screen
        window.tela_template._template_carregado = True
        window.tela_template.file_template = Mock()
        window.tela_template.ui.lineEdit_caminho_template.setText("/test/template.docx")
        
        # Set up patient screen
        window.tela_paciente.ui.lineEdit_nome.setText("Test Patient")
        window.tela_paciente.ui.dateEdit_nascimento.setDate(QDate(2010, 1, 1))
        
        # Navigate to collect data
        window.stacked_widget.setCurrentIndex(0)
        window._coletar_dados_tela_atual()
        
        assert window.data_model.template_path == "/test/template.docx"
        
        # Navigate to patient screen
        window.stacked_widget.setCurrentIndex(1)
        window._coletar_dados_tela_atual()
        
        assert window.data_model.patient_data["patient_name"] == "Test Patient"

