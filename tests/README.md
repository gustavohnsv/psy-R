# Test Suite for psy-R

This directory contains comprehensive automated tests following TDD (Test-Driven Development) principles for all branches of the psy-R application.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py                    # Shared fixtures and configuration
├── test_data_model.py             # Data Model tests
├── test_data_collection.py        # Data Collection tests
├── test_field_extraction.py       # Field Extraction and Validation tests
├── test_review_summary.py         # Review Screen Summary tests
├── test_document_generation.py    # Document Generation tests
├── test_integration_full_workflow.py # Integration and E2E tests
└── README.md
```

## Running Tests

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run Tests by Feature

```bash
# Data Model
pytest -m data_model

# Data Collection
pytest -m data_collection

# Field Extraction
pytest -m field_extraction

# Review Summary
pytest -m review_summary

# Document Generation
pytest -m document_generation
```

### Run Tests by Type

```bash
# Unit tests only
pytest -m unit

# Integration tests only
pytest -m integration

# End-to-end tests only
pytest -m e2e
```

### Run with Coverage

```bash
pytest --cov=src --cov-report=html
```

Coverage report will be generated in `htmlcov/index.html`

### Run Specific Test File

```bash
pytest tests/test_data_model.py
```

### Run Specific Test

```bash
pytest tests/test_data_model.py::TestLaudoDataModel::test_initialization
```

## Test Categories

### Unit Tests (`@pytest.mark.unit`)
- Test individual components in isolation
- Fast execution
- No external dependencies
- Examples: Data model methods, field validation, data collection

### Integration Tests (`@pytest.mark.integration`)
- Test interactions between components
- May use real file system or database
- Examples: Data flow between screens, template processing

### End-to-End Tests (`@pytest.mark.e2e`)
- Test complete workflows
- May require GUI components
- Slower execution
- Examples: Full document generation workflow

## Test Coverage

The test suite aims for:
- **Unit Tests**: 90%+ coverage of core logic
- **Integration Tests**: All major workflows covered
- **E2E Tests**: Critical user paths covered

## Writing New Tests

### Example Unit Test

```python
@pytest.mark.unit
@pytest.mark.data_model
class TestMyFeature:
    def test_my_function(self, sample_fixture):
        result = my_function(sample_fixture)
        assert result == expected_value
```

### Using Fixtures

Common fixtures are available in `conftest.py`:
- `sample_document`: Sample Document object
- `sample_patient_data`: Sample patient data dict
- `populated_data_model`: Fully populated data model
- `qapp`: QApplication instance for GUI tests

## Continuous Integration

Tests should be run:
- Before committing code
- In CI/CD pipeline
- Before merging branches

## Notes

- PDF conversion tests may be skipped in headless environments
- GUI tests require QApplication instance
- Some tests use mocks to avoid file system operations
- Test data is isolated using temporary directories

