from typing import Set, Dict, List, Tuple
from ..field_validator import FieldValidator

class TemplateValidator:
    """Service responsible for validating template fields."""
    
    def validate_fields(self, fields: Set[str]) -> Tuple[List[str], List[Tuple[str, str]]]:
        """Validate all fields against naming convention.
        
        Returns:
            Tuple of (valid_fields, invalid_fields_with_reasons)
        """
        return FieldValidator.validate_fields(list(fields))
    
    def check_required_fields(self, field_names: Set[str], available_data: Dict[str, str]) -> Tuple[List[str], List[str]]:
        """Check if all required fields have data.
        
        Returns:
            Tuple of (missing_fields, fields_with_empty_values)
        """
        missing_fields = []
        empty_fields = []
        
        for field_name in field_names:
            if field_name not in available_data:
                missing_fields.append(field_name)
            elif not available_data[field_name] or str(available_data[field_name]).strip() == "":
                empty_fields.append(field_name)
        
        return missing_fields, empty_fields
