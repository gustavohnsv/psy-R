from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class Patient:
    name: str = ""
    age: str = ""
    birthdate: str = ""
    school: str = ""
    group: str = ""


@dataclass
class TestEntry:
    test_id: str
    raw_values: Dict[str, Any] = field(default_factory=dict)
    converted_values: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ReportModel:
    patient: Patient = field(default_factory=Patient)
    tests: List[TestEntry] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_test(self, test_id: str, raw: Dict[str, Any]):
        self.tests.append(TestEntry(test_id=test_id, raw_values=raw))
