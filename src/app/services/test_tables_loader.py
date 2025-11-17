import json
from pathlib import Path
from typing import Dict, Any


class TestTablesLoader:
    """Load test configuration tables from src/app/data/*.jsonc.

    Files are JSON with // comments (jsonc). This loader strips simple // comments
    and parses the JSON.
    """

    def __init__(self, data_dir: Path | str | None = None):
        base = Path(data_dir) if data_dir else Path(__file__).resolve().parents[1] / "data"
        self.data_dir = base
        self._cache: Dict[str, Any] = {}

    def _load_jsonc(self, path: Path) -> Any:
        text = path.read_text(encoding="utf-8")
        # strip //... comments
        lines = []
        for line in text.splitlines():
            stripped = line
            if "//" in line:
                # remove inline comments
                stripped = line.split("//", 1)[0]
            lines.append(stripped)
        cleaned = "\n".join(lines)
        return json.loads(cleaned)

    def load_all(self) -> Dict[str, Any]:
        if self._cache:
            return self._cache

        files = list(self.data_dir.glob("*_table.jsonc"))
        for p in files:
            try:
                data = self._load_jsonc(p)
                key = p.stem.replace("_table", "")
                self._cache[key] = data
            except Exception:
                # skip files that fail to parse
                continue

        return self._cache

    def get(self, key: str) -> Dict[str, Any] | None:
        if not self._cache:
            self.load_all()
        return self._cache.get(key)
