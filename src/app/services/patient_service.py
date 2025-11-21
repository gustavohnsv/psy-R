from datetime import datetime, date
from typing import Optional

class PatientService:
    """Service responsible for patient-related logic."""
    
    @staticmethod
    def extract_first_name(full_name: str) -> str:
        """Extract the first name from a full name string."""
        if isinstance(full_name, str) and full_name.strip():
            return full_name.strip().split()[0]
        return ""

    @staticmethod
    def calculate_age(birth_date_str: str) -> Optional[str]:
        """Calculate chronological age from birth date string (DD/MM/YYYY)."""
        if not isinstance(birth_date_str, str) or not birth_date_str:
            return None
            
        try:
            # Attempt to parse common Brazilian format DD/MM/YYYY
            parsed = datetime.strptime(birth_date_str, "%d/%m/%Y").date()
            today = date.today()
            years = today.year - parsed.year - ((today.month, today.day) < (parsed.month, parsed.day))
            return str(years)
        except Exception:
            return None
