import re
from typing import List, Tuple, Set


class FieldValidator:
    """Validates field names against the program's naming convention."""
    
    # Define valid field name patterns
    PATTERNS = {
        'patient': re.compile(r'^patient_(name|birth|crono_age|school|class)$'),
        'resp1': re.compile(r'^resp1_(name|career|education|age)$'),
        'resp2': re.compile(r'^resp2_(name|career|education|age)$'),
        'psychologist': re.compile(r'^(nome_psicologo|crp_psicologo)$'),
        'conclusion': re.compile(r'^conclusao_text$'),
        'test_wisc': re.compile(r'^(QIT|ICV|IOP|IMO|IVP)(_out|_conclusao|_text_out)$'),
        'test_etdah': re.compile(r'^(F1|F2|F3|F4|TOTAL)_out$'),
        'test_etdah_conclusion': re.compile(r'^ETDAH_CONCLUSAO_BLOCO$'),
        'test_generic': re.compile(r'^[A-Z0-9_]+(_out|_conclusao|_text_out)$'),
    }
    
    @classmethod
    def validate_field_name(cls, field_name: str) -> Tuple[bool, str]:
        """Validate a single field name against naming convention.
        
        Args:
            field_name: The field name to validate (without braces)
            
        Returns:
            Tuple of (is_valid, reason)
        """
        # Check against all patterns
        for pattern_name, pattern in cls.PATTERNS.items():
            if pattern.match(field_name):
                return True, f"Valid {pattern_name} field"
        
        # If no pattern matches, it's invalid
        return False, f"Field '{field_name}' does not follow naming convention"
    
    @classmethod
    def validate_fields(cls, field_names: List[str]) -> Tuple[List[str], List[Tuple[str, str]]]:
        """Validate a list of field names.
        
        Args:
            field_names: List of field names to validate (without braces)
            
        Returns:
            Tuple of (valid_fields, invalid_fields_with_reasons)
            invalid_fields_with_reasons is a list of (field_name, reason) tuples
        """
        valid_fields = []
        invalid_fields = []
        
        for field_name in field_names:
            is_valid, reason = cls.validate_field_name(field_name)
            if is_valid:
                valid_fields.append(field_name)
            else:
                invalid_fields.append((field_name, reason))
        
        return valid_fields, invalid_fields
    
    @classmethod
    def get_expected_field_categories(cls) -> dict:
        """Get a dictionary of expected field categories and examples."""
        return {
            'patient': ['patient_name', 'patient_birth', 'patient_crono_age', 'patient_school', 'patient_class'],
            'respondent_1': ['resp1_name', 'resp1_career', 'resp1_education', 'resp1_age'],
            'respondent_2': ['resp2_name', 'resp2_career', 'resp2_education', 'resp2_age'],
            'psychologist': ['nome_psicologo', 'crp_psicologo'],
            'conclusion': ['conclusao_text'],
            'test_wisc': ['QIT_out', 'ICV_out', 'IOP_out', 'QIT_conclusao', 'ICV_text_out'],
            'test_etdah': ['F1_out', 'F2_out', 'F3_out', 'F4_out', 'TOTAL_out', 'ETDAH_CONCLUSAO_BLOCO'],
            'test_generic': ['Any uppercase field ending with _out, _conclusao, or _text_out']
        }

