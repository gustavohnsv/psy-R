"""Unit tests for Branch 4: Review Screen Summary."""
import pytest
from unittest.mock import Mock, MagicMock
from PySide6.QtWidgets import QApplication
import sys

# Ensure QApplication exists for GUI tests
if not QApplication.instance():
    app = QApplication(sys.argv)

# Check if ReviewScreen has data_model parameter (Branch 4 feature)
try:
    from app.views.review import ReviewScreen
    REVIEW_WITH_DATA_MODEL = True
except (ImportError, TypeError):
    REVIEW_WITH_DATA_MODEL = False


@pytest.mark.unit
@pytest.mark.branch4
@pytest.mark.skipif(not REVIEW_WITH_DATA_MODEL, reason="ReviewScreen data_model feature not available (Branch 4 not merged)")
class TestReviewScreen:
    """Test suite for ReviewScreen summary functionality."""
    
    def test_review_screen_initialization(self):
        """Test that ReviewScreen initializes correctly."""
        from app.views.review import ReviewScreen
        from app.models import LaudoDataModel
        
        data_model = LaudoDataModel()
        screen = ReviewScreen(data_model=data_model)
        
        assert screen.data_model == data_model
        assert screen.ui is not None
    
    def test_set_data_model(self):
        """Test setting data model after initialization."""
        from app.views.review import ReviewScreen
        from app.models import LaudoDataModel
        
        screen = ReviewScreen()
        data_model = LaudoDataModel()
        screen.set_data_model(data_model)
        
        assert screen.data_model == data_model
    
    def test_populate_summary_with_data(self, populated_data_model):
        """Test populating summary with data."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen(data_model=populated_data_model)
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        
        assert "Resumo dos Dados Coletados" in summary_text
        assert "João Silva" in summary_text
        assert "Maria Silva" in summary_text
        assert "José Silva" in summary_text
        assert "Dr. Ana Paula" in summary_text
    
    def test_populate_summary_without_data_model(self):
        """Test populating summary without data model."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen()
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        assert "Nenhum dado disponível" in summary_text
    
    def test_populate_summary_shows_field_mapping(self, populated_data_model):
        """Test that summary shows field mapping."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen(data_model=populated_data_model)
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        
        assert "Mapeamento de Campos" in summary_text
        assert "{patient_name}" in summary_text
        assert "João Silva" in summary_text
    
    def test_populate_summary_highlights_missing_fields(self):
        """Test that summary highlights missing fields."""
        from app.views.review import ReviewScreen
        from app.models import LaudoDataModel
        
        # Create model with some missing data
        model = LaudoDataModel()
        model.set_patient_data({"patient_name": "Test"})
        # Leave other fields empty
        
        screen = ReviewScreen(data_model=model)
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        
        # Should show warnings for missing data
        assert "não preenchidos" in summary_text or "VAZIO" in summary_text
    
    def test_populate_summary_shows_template_path(self, populated_data_model):
        """Test that summary shows template path."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen(data_model=populated_data_model)
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        assert "/test/path/template.docx" in summary_text
    
    def test_populate_summary_shows_test_results(self, populated_data_model):
        """Test that summary shows test results."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen(data_model=populated_data_model)
        screen.populate_summary()
        
        summary_text = screen.ui.label_revisao.text()
        assert "Resultados dos Testes" in summary_text
        assert "QIT_out" in summary_text or "105" in summary_text


@pytest.mark.integration
@pytest.mark.branch4
@pytest.mark.skipif(not REVIEW_WITH_DATA_MODEL, reason="ReviewScreen data_model feature not available (Branch 4 not merged)")
class TestReviewScreenIntegration:
    """Integration tests for ReviewScreen."""
    
    def test_review_screen_updates_on_show(self, populated_data_model, qapp):
        """Test that review screen updates when shown."""
        from app.views.review import ReviewScreen
        
        screen = ReviewScreen(data_model=populated_data_model)
        
        # Initially summary might be empty or default
        initial_text = screen.ui.label_revisao.text()
        
        # Simulate show event
        from PySide6.QtGui import QShowEvent
        event = QShowEvent()
        screen.showEvent(event)
        
        # Summary should now be populated
        final_text = screen.ui.label_revisao.text()
        assert len(final_text) > len(initial_text) or "Resumo" in final_text

