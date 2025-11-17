import json
from pathlib import Path
from typing import Dict, Iterable, Optional, Any


class TemplateFieldsLoader:
    """Loads the configuration that describes non-test template placeholders."""

    def __init__(self, config_path: Optional[Path | str] = None):
        base_path = Path(config_path) if config_path else Path(__file__).resolve().parents[1] / "data" / "template_fields.json"
        self.config_path = base_path
        self._cache: Optional[Dict[str, Any]] = None

    def load_config(self) -> Dict[str, Any]:
        """Load JSON configuration that describes the editable fields."""
        if self._cache is None:
            with self.config_path.open("r", encoding="utf-8") as fp:
                self._cache = json.load(fp)
        return self._cache

    def get_all_fields(self) -> Dict[str, Dict[str, Any]]:
        """Return a mapping of field names to their configuration."""
        fields: Dict[str, Dict[str, Any]] = {}
        config = self.load_config()
        for section in config.get("sections", []):
            for field in section.get("fields", []):
                fields[field["name"]] = field
        return fields

    def iter_sections(self) -> Iterable[Dict[str, Any]]:
        """Iterate over configured sections."""
        config = self.load_config()
        return config.get("sections", [])

