"""Unit tests for Branch 1: Data Model and Storage."""
import pytest
from docx import Document
from app.models import LaudoDataModel


@pytest.mark.unit
@pytest.mark.data_model
class TestLaudoDataModel:
    """Test suite for LaudoDataModel class."""
    
    def test_initialization(self):
        """Test that data model initializes with empty/default values."""
        model = LaudoDataModel()
        
        assert model.template_path is None
        assert model.template_document is None
        assert model.patient_data["patient_name"] == ""
        assert model.resp1_data["resp1_name"] == ""
        assert model.resp2_data["resp2_name"] == ""
        assert model.test_results == {}
        assert model.conclusion_text == ""
        assert model.psychologist_data["nome_psicologo"] == ""
        assert not model.is_template_loaded()
    
    def test_set_template(self, sample_document):
        """Test setting template path and document."""
        model = LaudoDataModel()
        model.set_template("/test/path/template.docx", sample_document)
        
        assert model.template_path == "/test/path/template.docx"
        assert model.template_document == sample_document
        assert model.is_template_loaded()
    
    def test_set_patient_data(self, sample_patient_data):
        """Test setting patient data."""
        model = LaudoDataModel()
        model.set_patient_data(sample_patient_data)
        
        for key, value in sample_patient_data.items():
            assert model.patient_data[key] == value
    
    def test_set_resp1_data(self, sample_resp1_data):
        """Test setting respondent 1 data."""
        model = LaudoDataModel()
        model.set_resp1_data(sample_resp1_data)
        
        for key, value in sample_resp1_data.items():
            assert model.resp1_data[key] == value
    
    def test_set_resp2_data(self, sample_resp2_data):
        """Test setting respondent 2 data."""
        model = LaudoDataModel()
        model.set_resp2_data(sample_resp2_data)
        
        for key, value in sample_resp2_data.items():
            assert model.resp2_data[key] == value
    
    def test_set_test_results(self, sample_test_results):
        """Test setting test results."""
        model = LaudoDataModel()
        model.set_test_results(sample_test_results)
        
        for key, value in sample_test_results.items():
            assert model.test_results[key] == value
    
    def test_set_conclusion_text(self, sample_conclusion_text):
        """Test setting conclusion text."""
        model = LaudoDataModel()
        model.set_conclusion_text(sample_conclusion_text)
        
        assert model.conclusion_text == sample_conclusion_text
    
    def test_set_psychologist_data(self, sample_psychologist_data):
        """Test setting psychologist data."""
        model = LaudoDataModel()
        model.set_psychologist_data(sample_psychologist_data)
        
        for key, value in sample_psychologist_data.items():
            assert model.psychologist_data[key] == value
    
    def test_get_all_data(self, populated_data_model):
        """Test getting all data as dictionary."""
        all_data = populated_data_model.get_all_data()
        
        assert isinstance(all_data, dict)
        assert "template_path" in all_data
        assert "patient" in all_data
        assert "resp1" in all_data
        assert "resp2" in all_data
        assert "tests" in all_data
        assert "conclusion" in all_data
        assert "psychologist" in all_data
        assert all_data["patient"]["patient_name"] == "João Silva"
    
    def test_get_field_mapping(self, populated_data_model):
        """Test getting field mapping for template replacement."""
        field_mapping = populated_data_model.get_field_mapping()
        
        assert isinstance(field_mapping, dict)
        assert "patient_name" in field_mapping
        assert "resp1_name" in field_mapping
        assert "resp2_name" in field_mapping
        assert "conclusao_text" in field_mapping
        assert "nome_psicologo" in field_mapping
        assert field_mapping["patient_name"] == "João Silva"
        assert all(isinstance(v, str) for v in field_mapping.values())
    
    def test_to_dict(self, populated_data_model):
        """Test converting model to dictionary."""
        dict_repr = populated_data_model.to_dict()
        
        assert isinstance(dict_repr, dict)
        assert dict_repr == populated_data_model.get_all_data()
    
    def test_partial_update_preserves_other_fields(self, sample_patient_data):
        """Test that partial updates preserve other fields."""
        model = LaudoDataModel()
        model.set_patient_data(sample_patient_data)
        
        # Update only one field
        model.set_patient_data({"patient_name": "Updated Name"})
        
        assert model.patient_data["patient_name"] == "Updated Name"
        assert model.patient_data["patient_birth"] == sample_patient_data["patient_birth"]
        assert model.patient_data["patient_school"] == sample_patient_data["patient_school"]
    
    def test_is_template_loaded(self, sample_document):
        """Test template loaded check."""
        model = LaudoDataModel()
        assert not model.is_template_loaded()
        
        model.set_template("/test/path.docx", sample_document)
        assert model.is_template_loaded()
        
        model.template_path = None
        assert not model.is_template_loaded()
    
    def test_field_mapping_includes_all_data_types(self, populated_data_model):
        """Test that field mapping includes all data types correctly."""
        field_mapping = populated_data_model.get_field_mapping()
        
        # Check patient fields
        assert field_mapping["patient_name"] == "João Silva"
        assert field_mapping["patient_birth"] == "15/03/2010"
        
        # Check respondent fields
        assert field_mapping["resp1_name"] == "Maria Silva"
        assert field_mapping["resp1_age"] == "35"  # Converted to string
        assert field_mapping["resp2_name"] == "José Silva"
        
        # Check test results
        assert field_mapping["QIT_out"] == "105"
        
        # Check conclusion
        assert field_mapping["conclusao_text"] == "Este é um texto de conclusão de teste."
        
        # Check psychologist
        assert field_mapping["nome_psicologo"] == "Dr. Ana Paula"

