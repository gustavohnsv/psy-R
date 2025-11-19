from docx import Document
from typing import Dict, Optional, Any

from app.services.test_result_classifier import TestResultClassifier


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
        self._test_classifier = TestResultClassifier()
        
        # Conclusion text
        self.conclusion_text: str = ""

        # Template fields not covered by other screens
        self.template_fields_data: Dict[str, Any] = {}
        
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
        # Update provided fields first
        self.patient_data.update(data)

        # Compute derived fields when possible
        # 1) First name (primeiro nome)
        full_name = self.patient_data.get("patient_name", "") or ""
        first_name = ""
        if isinstance(full_name, str) and full_name.strip():
            first_name = full_name.strip().split()[0]
        # store under a conventional key used in templates mapping
        self.patient_data["patient_first_name"] = first_name

        # 2) Chronological age (years) from `patient_birth` if not provided
        # Only compute if caller did not supply `patient_crono_age` (preserve explicit values)
        birth = self.patient_data.get("patient_birth", "") or ""
        provided_crono = self.patient_data.get("patient_crono_age")
        if (provided_crono is None or provided_crono == "") and isinstance(birth, str) and birth:
            try:
                from datetime import datetime, date

                # Attempt to parse common Brazilian format DD/MM/YYYY
                parsed = datetime.strptime(birth, "%d/%m/%Y").date()
                today = date.today()
                years = today.year - parsed.year - ((today.month, today.day) < (parsed.month, parsed.day))
                self.patient_data["patient_crono_age"] = str(years)
            except Exception:
                # parsing failed: leave as empty string
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
        """Get a flat dictionary mapping field names to values for template replacement.
        
        Returns a dictionary where keys are template field names (e.g., {nome_paciente})
        and values are the actual data to replace them with.
        Maps both standard field names and template-specific field names.
        """
        mapping = {}
        
        # Field name translation map: data_model_key -> [template_field_names]
        field_translations = {
            # Patient fields
            "patient_name": ["nome_paciente", "primeiro_nome_paciente"],
            "patient_birth": ["data_nasc_paciente"],
            "patient_crono_age": ["idd_paciente"],
            "patient_school": ["escola_paciente"],
            "patient_class": ["turma_paciente"],
            
            # Respondent 1 fields
            "resp1_name": ["resp1_nome"],
            "resp1_career": ["resp1_profissao"],
            "resp1_education": ["resp1_escolaridade"],
            "resp1_age": ["resp1_idade"],
            
            # Respondent 2 fields
            "resp2_name": ["resp2_nome"],
            "resp2_career": ["resp2_profissao"],
            "resp2_education": ["resp2_escolaridade"],
            "resp2_age": ["resp2_idade"],
            
            # Psychologist fields
            "nome_psicologo": ["psico_nome"],
            "crp_psicologo": ["psico_crp"],
        }
        
        # Add patient fields with both standard and template names
        for key, value in self.patient_data.items():
            # Add standard name
            mapping[key] = str(value) if value is not None else ""
            # Add template-specific names
            if key in field_translations:
                for template_name in field_translations[key]:
                    mapping[template_name] = str(value) if value is not None else ""

        # Ensure primeiro nome (first name) placeholder maps to the first token of full name
        # Templates use the alias `primeiro_nome_paciente` which should contain only the first name
        if "patient_name" in mapping:
            try:
                first = mapping["patient_name"].strip().split()[0]
            except Exception:
                first = ""
            mapping.setdefault("primeiro_nome_paciente", first)
        
        # Add respondent 1 fields with both standard and template names
        for key, value in self.resp1_data.items():
            # Add standard name
            mapping[key] = str(value) if value is not None else ""
            # Add template-specific names
            if key in field_translations:
                for template_name in field_translations[key]:
                    mapping[template_name] = str(value) if value is not None else ""
        
        # Add respondent 2 fields with both standard and template names
        for key, value in self.resp2_data.items():
            # Add standard name
            mapping[key] = str(value) if value is not None else ""
            # Add template-specific names
            if key in field_translations:
                for template_name in field_translations[key]:
                    mapping[template_name] = str(value) if value is not None else ""
        
        # Test result fields with optional aliases for template compatibility
        test_field_translations = {
            "AG_BPA": ["AG_pontuacao"],
        }

        for key, value in self.test_results.items():
            str_value = str(value) if value is not None else ""
            mapping[key] = str_value
            if key in test_field_translations:
                for alias in test_field_translations[key]:
                    mapping.setdefault(alias, str_value)
        
        # Conclusion field
        mapping["conclusao_text"] = self.conclusion_text

        # Custom template fields
        for key, value in self.template_fields_data.items():
            mapping[key] = str(value) if value is not None else ""
        
        # Psychologist fields with both standard and template names
        for key, value in self.psychologist_data.items():
            # Add standard name
            mapping[key] = str(value) if value is not None else ""
            # Add template-specific names
            if key in field_translations:
                for template_name in field_translations[key]:
                    mapping[template_name] = str(value) if value is not None else ""
        
        return mapping
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the entire model to a dictionary representation."""
        return self.get_all_data()
    
    def is_template_loaded(self) -> bool:
        """Check if template is loaded."""
        return self.template_path is not None and self.template_document is not None

