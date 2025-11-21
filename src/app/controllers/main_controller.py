import os
from typing import Optional
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog, QMainWindow

from app.models.data_model import ReportDataModel
from app.services.template_processor import TemplateProcessor
from app.views import (
    TemplateScreen,
    PatientScreen,
    TemplateFieldsScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen,
)

class MainController:
    """Main controller orchestrating application logic and data flow."""
    
    def __init__(self, main_window: QMainWindow, data_model: ReportDataModel):
        self.main_window = main_window
        self.data_model = data_model
        
    def collect_data_from_current_view(self):
        """Collect data from the currently visible screen into the data model."""
        stacked_widget = self.main_window.stacked_widget
        widget = stacked_widget.currentWidget()
        
        if isinstance(widget, TemplateScreen):
            self._collect_template_data(widget)
        elif isinstance(widget, PatientScreen):
            self._collect_patient_data(widget)
        elif isinstance(widget, TemplateFieldsScreen):
            self._collect_template_fields_data(widget)
        elif isinstance(widget, TestsScreen):
            self._collect_tests_data(widget)
        elif isinstance(widget, ConclusionScreen):
            self._collect_conclusion_data(widget)
        elif isinstance(widget, ReviewScreen):
            # Review screen is read-only mostly, but good to have hook
            pass
            
    def prepare_view(self, index: int):
        """Prepare a view before it is shown (e.g. populate with data)."""
        widget = self.main_window.stacked_widget.widget(index)
        
        if isinstance(widget, TemplateFieldsScreen):
            widget.set_data(self.data_model.get_template_field_values())
        elif isinstance(widget, ConclusionScreen):
            widget.refresh_calculated_data()
        elif isinstance(widget, ReviewScreen):
            # Ensure conclusion is up to date in model before showing review
            # (This might be redundant if collect_data was called, but safe)
            pass

    def _collect_template_data(self, widget: TemplateScreen):
        path = widget.get_template_path()
        doc = widget.get_template_document()
        if path and doc:
            self.data_model.set_template(path, doc)

    def _collect_patient_data(self, widget: PatientScreen):
        data = widget.get_data()
        if "patient" in data:
            self.data_model.set_patient_data(data["patient"])
        if "resp1" in data:
            self.data_model.set_resp1_data(data["resp1"])
        if "resp2" in data:
            self.data_model.set_resp2_data(data["resp2"])
        if "template_fields" in data:
            self.data_model.set_template_field_values(data["template_fields"])

    def _collect_template_fields_data(self, widget: TemplateFieldsScreen):
        data = widget.get_data()
        if data:
            self.data_model.set_template_field_values(data)
            
        # Special handling for conclusions section
        if "CONCLUSAO_ANALISE_LIVRE" in data:
            self.data_model.set_conclusion_text(data.get("CONCLUSAO_ANALISE_LIVRE", ""))
        elif "conclusion_text" in data:
            self.data_model.set_conclusion_text(data.get("conclusion_text", ""))

    def _collect_tests_data(self, widget: TestsScreen):
        data = widget.get_data()
        if data:
            self.data_model.set_test_results(data)
            # Notify conclusion screen to update if it exists
            if hasattr(self.main_window, "conclusion_screen"):
                self.main_window.conclusion_screen.refresh_calculated_data()

    def _collect_conclusion_data(self, widget: ConclusionScreen):
        data = widget.get_data()
        if "conclusion_text" in data:
            self.data_model.set_conclusion_text(data["conclusion_text"])

    def generate_report(self):
        """Handle the report generation process."""
        # Ensure current screen data is collected
        self.collect_data_from_current_view()
        
        if not self.data_model.is_template_loaded():
            QMessageBox.critical(
                self.main_window,
                'Erro',
                'Nenhum template foi carregado. Por favor, carregue um template antes de gerar o laudo.'
            )
            return

        processor = TemplateProcessor(self.data_model.template_document)
        
        # Validation
        valid_fields, invalid_fields = processor.validate_fields()
        if invalid_fields:
            invalid_list = '\n'.join([f"  - {field}: {reason}" for field, reason in invalid_fields])
            reply = QMessageBox.warning(
                self.main_window,
                'Campos Inválidos Encontrados',
                f'O template contém campos que não seguem a convenção de nomenclatura:\n\n{invalid_list}\n\n'
                'Deseja continuar mesmo assim?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return

        # Check required fields
        field_mapping = self.data_model.get_field_mapping()
        template_fields = processor.extract_fields()
        missing_fields, empty_fields = processor.check_required_fields(template_fields, field_mapping)
        
        if missing_fields or empty_fields:
            warning_parts = []
            if missing_fields:
                warning_parts.append(f"Campos faltando: {', '.join(missing_fields)}")
            if empty_fields:
                warning_parts.append(f"Campos vazios: {', '.join(empty_fields)}")
            
            warning_text = '\n\n'.join(warning_parts)
            reply = QMessageBox.warning(
                self.main_window,
                'Campos Incompletos',
                f'Os seguintes campos não têm dados:\n\n{warning_text}\n\n'
                'Deseja continuar mesmo assim? Os campos vazios serão deixados em branco no documento.',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return

        # Select output directory
        output_dir = QFileDialog.getExistingDirectory(
            self.main_window,
            'Selecione o diretório para salvar o laudo',
            os.path.expanduser('~')
        )
        
        if not output_dir:
            return

        try:
            # Process and save
            from docx import Document
            template_copy = Document(self.data_model.template_path)
            processor.set_document(template_copy)
            processor.replace_fields(field_mapping, template_copy)
            
            patient_name = self.data_model.patient_data.get("patient_name", "").strip()
            if patient_name:
                safe_name = "".join(c for c in patient_name if c.isalnum() or c in (' ', '-', '_')).strip()
                safe_name = safe_name.replace(' ', '_')
                base_filename = f"laudo_{safe_name}"
            else:
                base_filename = "laudo"
            
            docx_path = os.path.join(output_dir, f"{base_filename}.docx")
            processor.save_document(template_copy, docx_path)
            
            QMessageBox.information(
                self.main_window,
                'Sucesso',
                f'Laudo gerado com sucesso!\n\n'
                f'DOCX: {docx_path}\n'
            )
            
        except Exception as e:
            QMessageBox.critical(
                self.main_window,
                'Erro ao Gerar Laudo',
                f'Ocorreu um erro ao gerar o laudo:\n\n{str(e)}'
            )
