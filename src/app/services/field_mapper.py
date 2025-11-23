from typing import Dict, Any, List

class FieldMapperService:
    """Service responsible for mapping data model fields to template placeholders."""
    
    def __init__(self):
        self.field_translations = {
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
            "psychologist_name": ["psico_nome", "nome_psicologo"],
            "psychologist_crp": ["psico_crp", "crp_psicologo"],
        }
        
        self.test_field_translations = {
            "AG_BPA": ["AG_pontuacao"],
        }

    def get_field_mapping(self, all_data: Dict[str, Any]) -> Dict[str, str]:
        """Get a flat dictionary mapping field names to values for template replacement."""
        mapping = {}
        
        patient_data = all_data.get("patient", {})
        resp1_data = all_data.get("resp1", {})
        resp2_data = all_data.get("resp2", {})
        test_results = all_data.get("tests", {})
        conclusion_text = all_data.get("conclusion", "")
        psychologist_data = all_data.get("psychologist", {})
        template_fields_data = all_data.get("template_fields", {})

        # Helper to add fields with translations
        def add_fields(source_data: Dict[str, Any]):
            for key, value in source_data.items():
                # Add standard name
                mapping[key] = str(value) if value is not None else ""
                # Add template-specific names
                if key in self.field_translations:
                    for template_name in self.field_translations[key]:
                        mapping[template_name] = str(value) if value is not None else ""

        add_fields(patient_data)
        add_fields(resp1_data)
        add_fields(resp2_data)
        add_fields(psychologist_data)

        # Ensure primeiro nome (first name) placeholder maps to the first token of full name
        if "patient_name" in mapping:
            try:
                first = mapping["patient_name"].strip().split()[0]
            except Exception:
                first = ""
            mapping.setdefault("primeiro_nome_paciente", first)

        # Test result fields
        for key, value in test_results.items():
            str_value = str(value) if value is not None else ""
            mapping[key] = str_value
            if key in self.test_field_translations:
                for alias in self.test_field_translations[key]:
                    mapping.setdefault(alias, str_value)
        
        # Conclusion field
        mapping["conclusion_text"] = conclusion_text
        # Backward compatibility
        mapping["conclusao_text"] = conclusion_text

        # Custom template fields
        for key, value in template_fields_data.items():
            mapping[key] = str(value) if value is not None else ""
            
        return mapping
