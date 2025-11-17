## Purpose

Quick, focused guidance for AI coding assistants working on this repository (psy-R).
Include only immediately-useful, discoverable facts and concrete examples from the codebase.

## Big picture (what this app is)
- Desktop GUI written with PySide6. Entry point: `src/main.py` (creates `MainWindow`).
- Single-window flow of screens managed by a QStackedWidget. Screens live in `src/app/views/`.
- Single source-of-truth data model: `src/app/models/data_model.py` defines `LaudoDataModel`.
- Template processing and validation live under `src/app/services/` (example: `TemplateProcessor`).

Why this matters: UI screens call `get_data()` / `set_data()` and the `MainWindow` copies those into the shared `LaudoDataModel`; template replacement uses `LaudoDataModel.get_field_mapping()` to produce a dict of template keys -> values.

## Key files to reference (quick links)
- `src/main.py` — wiring of screens, navigation callbacks, and document generation flow.
- `src/app/models/data_model.py` — canonical data shapes and `get_field_mapping()` behavior.
- `src/app/services/template_processor.py` — extraction, validation, replacement and saving of DOCX templates (uses `python-docx`).
- `src/app/data/template_fields.json` — canonical template field definitions and expected names.
- `src/app/views/` — UI screens; note signal names like `avancar_clicado` and `voltar_clicado` (Portuguese naming).
- `tests/conftest.py` and `tests/test_data_model.py` — example fixtures (`sample_document`, `populated_data_model`) and expectations for `LaudoDataModel` behavior.

## Concrete patterns & conventions (do follow these)
- Language: code mixes English and Portuguese identifiers. Keep local names consistent with existing screens (e.g. `avancar_clicado`).
- Data model is authoritative: prefer reading/writing via `LaudoDataModel` methods (`set_patient_data`, `set_template`, `get_field_mapping`, etc.).
- Template fields in DOCX use simple placeholders (see tests: `{patient_name}`) and the processor expects string values — `get_field_mapping()` converts values to `str`.
- Field naming: both canonical keys (e.g. `patient_name`) and template aliases (e.g. `nome_paciente`, `psico_nome`) are used; add new aliases in `LaudoDataModel.get_field_mapping()` when necessary.
- UI files (.ui) are compiled to Python with `pyside6-uic` — script: `update.sh` (run in repo root) compiles `src/app/views/ui_files/*.ui` into `src/app/views/ui_*.py`.

## How to run / test (developer workflows)
- Run the GUI (development):
  - From repo root: `./run.sh` (this does `cd src && python main.py`).
- Regenerate compiled UI modules after editing `.ui` files: `./update.sh`.
- Run test suite (configured in `pytest.ini`): from repo root run `pytest`. The project `pytest.ini` already adds coverage and HTML report options.
  - Run a focused unit test: `pytest tests/test_data_model.py::TestLaudoDataModel::test_initialization -q`.

## Tests & fixtures to follow for examples
- `tests/conftest.py` shows typical fixtures (e.g. `sample_document`, `sample_patient_data`, `populated_data_model`). Use these fixtures in new tests.
- Tests use markers defined in `pytest.ini` (e.g. `unit`, `integration`, `data_model`). Use `-m unit` to run unit tests only.

## Integration points & external dependencies
- `python-docx` for reading/writing .docx files (see `TemplateProcessor` and `LaudoDataModel.set_template`).
- `docx2pdf` may be used to generate PDFs from DOCX in the generation flow.
- `pyside6` for the GUI; ensure tests that import Qt use the `qapp` fixture from `tests/conftest.py`.
- Packaging/build: `pyinstaller` is included in `requirements.txt` (used by the maintainer for distributions).

## Small examples you can copy-paste
- Use the central model to get a replacement mapping:

  Example: `from app.models import LaudoDataModel; mapping = LaudoDataModel().get_field_mapping()`

  TemplateProcessor expects a mapping where keys match `template_fields.json` names (e.g. `nome_psicologo`, `CONCLUSAO_ANALISE_LIVRE`).

## Notes for AI agents
- Prefer minimal, test-covered changes. Reference and run unit tests in `tests/` for any behavior you touch.
- Keep translations/aliases in `get_field_mapping()` consistent with `src/app/data/template_fields.json`.
- Avoid renaming public screen signals or data model keys without updating `src/main.py` and tests. These are tightly coupled.

## If you add or change template fields
1. Update `src/app/data/template_fields.json` (add field name + label).
2. If you require aliasing to existing data model keys, update `LaudoDataModel.get_field_mapping()` so the template name maps to a string value.
3. Add/extend tests under `tests/` using existing fixtures (see `populated_data_model`).

---
If any of the above is unclear or you'd like me to include additional examples (e.g. a minimal test that demonstrates adding a new template field), tell me which area to expand.
