from docx import Document
from typing import Dict, Optional, Any

from app.services.test_result_classifier import TestResultClassifier
from app.services.field_mapper import FieldMapperService
from app.services.patient_service import PatientService


class ReportDataModel:
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
        self._test_classifier = TestResultClassifier()
        
        # Conclusion text
        self.conclusion_text: str = ""

        # Template fields not covered by other screens
        self.template_fields_data: Dict[str, Any] = {}
        
        # Psychologist metadata
        self.psychologist_data: Dict[str, Any] = {
            "psychologist_name": "",
            "psychologist_crp": ""
        }
        
        self._field_mapper = FieldMapperService()
    
    def set_template(self, path: str, document: Document):
        """Set the template path and document."""
        self.template_path = path
        self.template_document = document
    
    def set_patient_data(self, data: Dict[str, Any]):
        """Update patient data."""
        # Update provided fields first
        self.patient_data.update(data)

        # Compute derived fields when possible
        # 1) First name (primeiro nome)
        full_name = self.patient_data.get("patient_name", "") or ""
        self.patient_data["patient_first_name"] = PatientService.extract_first_name(full_name)

        # 2) Chronological age (years) from `patient_birth` if not provided
        # Only compute if caller did not supply `patient_crono_age` (preserve explicit values)
        birth = self.patient_data.get("patient_birth", "") or ""
        provided_crono = self.patient_data.get("patient_crono_age")
        
        if (provided_crono is None or provided_crono == "") and isinstance(birth, str) and birth:
            age = PatientService.calculate_age(birth)
            if age:
                self.patient_data["patient_crono_age"] = age
            else:
                self.patient_data["patient_crono_age"] = str(provided_crono or "")
        else:
            # Preserve caller-provided value
            self.patient_data["patient_crono_age"] = str(provided_crono or "")
    
    def set_resp1_data(self, data: Dict[str, Any]):
        """Update first respondent data."""
        self.resp1_data.update(data)
    
    def set_resp2_data(self, data: Dict[str, Any]):
        """Update second respondent data."""
        self.resp2_data.update(data)
    
    def set_test_results(self, results: Dict[str, Any]):
        """Update test results."""
        if not isinstance(results, dict):
            return

        try:
            classified = self._test_classifier.classify_results(results)
        except Exception:
            classified = results

        self.test_results.update(classified)
    
    def set_conclusion_text(self, text: str):
        """Set conclusion text."""
        self.conclusion_text = text
    
    def set_template_field_values(self, values: Dict[str, Any]):
        """Update custom template field values."""
        self.template_fields_data.update(values)
    
    def get_template_field_values(self) -> Dict[str, Any]:
        """Return stored template field values."""
        return self.template_fields_data
    
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
            "psychologist": self.psychologist_data,
            "template_fields": self.template_fields_data
        }
    
    def get_field_mapping(self) -> Dict[str, str]:
        """Get a flat dictionary mapping field names to values for template replacement."""
        return self._field_mapper.get_field_mapping(self.get_all_data())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the entire model to a dictionary representation."""
        return self.get_all_data()
    
    def is_template_loaded(self) -> bool:
        """Check if template is loaded."""
        return self.template_path is not None and self.template_document is not None


