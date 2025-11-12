from docx import Document
from typing import Dict, Optional, Any


class LaudoDataModel:
    """Central data model to store all collected data for psychological report generation."""
    
    def __init__(self):
        # Template data
        self.template_path: Optional[str] = None
        self.template_document: Optional[Document] = None
        
        # Patient data
        self.patient_data: Dict[str, Any] = {
            "patient_name": "",
            "patient_birth": "",
            "patient_crono_age": "",
            "patient_school": "",
            "patient_class": ""
        }
        
        # Respondent data
        self.resp1_data: Dict[str, Any] = {
            "resp1_name": "",
            "resp1_career": "",
            "resp1_education": "",
            "resp1_age": 0
        }
        
        self.resp2_data: Dict[str, Any] = {
            "resp2_name": "",
            "resp2_career": "",
            "resp2_education": "",
            "resp2_age": 0
        }
        
        # Test results
        self.test_results: Dict[str, Any] = {}
        
        # Conclusion text
        self.conclusion_text: str = ""
        
        # Psychologist metadata
        self.psychologist_data: Dict[str, Any] = {
            "nome_psicologo": "",
            "crp_psicologo": ""
        }
    
    def set_template(self, path: str, document: Document):
        """Set the template path and document."""
        self.template_path = path
        self.template_document = document
    
    def set_patient_data(self, data: Dict[str, Any]):
        """Update patient data."""
        self.patient_data.update(data)
    
    def set_resp1_data(self, data: Dict[str, Any]):
        """Update first respondent data."""
        self.resp1_data.update(data)
    
    def set_resp2_data(self, data: Dict[str, Any]):
        """Update second respondent data."""
        self.resp2_data.update(data)
    
    def set_test_results(self, results: Dict[str, Any]):
        """Update test results."""
        self.test_results.update(results)
    
    def set_conclusion_text(self, text: str):
        """Set conclusion text."""
        self.conclusion_text = text
    
    def set_psychologist_data(self, data: Dict[str, Any]):
        """Update psychologist data."""
        self.psychologist_data.update(data)
    
    def get_all_data(self) -> Dict[str, Any]:
        """Get all collected data as a dictionary."""
        return {
            "template_path": self.template_path,
            "patient": self.patient_data,
            "resp1": self.resp1_data,
            "resp2": self.resp2_data,
            "tests": self.test_results,
            "conclusion": self.conclusion_text,
            "psychologist": self.psychologist_data
        }
    
    def get_field_mapping(self) -> Dict[str, str]:
        """Get a flat dictionary mapping field names to values for template replacement.
        
        Returns a dictionary where keys are template field names (e.g., {patient_name})
        and values are the actual data to replace them with.
        """
        mapping = {}
        
        # Patient fields
        for key, value in self.patient_data.items():
            mapping[key] = str(value) if value is not None else ""
        
        # Respondent 1 fields
        for key, value in self.resp1_data.items():
            mapping[key] = str(value) if value is not None else ""
        
        # Respondent 2 fields
        for key, value in self.resp2_data.items():
            mapping[key] = str(value) if value is not None else ""
        
        # Test result fields
        for key, value in self.test_results.items():
            mapping[key] = str(value) if value is not None else ""
        
        # Conclusion field
        mapping["conclusao_text"] = self.conclusion_text
        
        # Psychologist fields
        for key, value in self.psychologist_data.items():
            mapping[key] = str(value) if value is not None else ""
        
        return mapping
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the entire model to a dictionary representation."""
        return self.get_all_data()
    
    def is_template_loaded(self) -> bool:
        """Check if template is loaded."""
        return self.template_path is not None and self.template_document is not None

