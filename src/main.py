import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QFileDialog, QMessageBox
from docx import Document

from app.views import (
    TemplateScreen,
    PatientScreen,
    TemplateFieldsScreen,
    TestsScreen,
    ReviewScreen,
)
from app.models import LaudoDataModel
from app.services import TemplateProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PsiqueLaudo")
        self.resize(800, 600)

        # Initialize data model
        self.data_model = LaudoDataModel()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.criar_e_conectar_telas()
        self.stacked_widget.setCurrentIndex(0)

    def criar_e_conectar_telas(self):

        self.tela_template = TemplateScreen()
        self.tela_paciente = PatientScreen()
        # Split template fields into focused screens (administrative, clinical, behavior, conclusions)
        self.tela_campos_administrativo = TemplateFieldsScreen()
        self.tela_campos_administrativo.set_sections(["administrativo"])

        self.tela_campos_contexto = TemplateFieldsScreen()
        self.tela_campos_contexto.set_sections(["contexto_clinico"])

        self.tela_campos_comportamento = TemplateFieldsScreen()
        self.tela_campos_comportamento.set_sections(["comportamento_observado"])
        # Conclusions use the same dynamic screen but restricted to the conclusions section
        self.tela_conclusoes_section = TemplateFieldsScreen()
        self.tela_conclusoes_section.set_sections(["conclusoes"])

        # Keep a backward-compatible separate ConclusionScreen instance (some tests / callers expect it)
        from app.views.conclusion import ConclusionScreen
        self.tela_conclusao = ConclusionScreen()

        self.tela_testes = TestsScreen()
        self.tela_revisao = ReviewScreen(data_model=self.data_model)

        # Order: template -> patient -> admin fields -> clinical -> behavior -> tests -> conclusions -> review
        self.stacked_widget.addWidget(self.tela_template)
        self.stacked_widget.addWidget(self.tela_paciente)
        self.stacked_widget.addWidget(self.tela_campos_administrativo)
        self.stacked_widget.addWidget(self.tela_campos_contexto)
        self.stacked_widget.addWidget(self.tela_campos_comportamento)
        self.stacked_widget.addWidget(self.tela_testes)
        # add both conclusions widgets (conclusions section and legacy conclusion screen) to preserve API/indices
        self.stacked_widget.addWidget(self.tela_conclusoes_section)
        self.stacked_widget.addWidget(self.tela_conclusao)
        self.stacked_widget.addWidget(self.tela_revisao)

        self.tela_template.avancar_clicado.connect(self.ir_para_proxima_tela)

        self.tela_paciente.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_paciente.voltar_clicado.connect(self.ir_para_tela_anterior)

        for tela in (self.tela_campos_administrativo, self.tela_campos_contexto, self.tela_campos_comportamento, self.tela_conclusoes_section):
            tela.avancar_clicado.connect(self.ir_para_proxima_tela)
            tela.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_testes.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_testes.voltar_clicado.connect(self.ir_para_tela_anterior)

        # conclusions section leads to review
        self.tela_conclusoes_section.avancar_clicado.connect(self._ir_para_revisao)
        self.tela_conclusoes_section.voltar_clicado.connect(self.ir_para_tela_anterior)

        # wire legacy conclusion screen as before (backward compatibility)
        self.tela_conclusao.avancar_clicado.connect(self._ir_para_revisao)
        self.tela_conclusao.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_revisao.voltar_clicado.connect(self.ir_para_tela_anterior)
        self.tela_revisao.gerar_laudo_clicado.connect(self.gerar_laudo)

    def ir_para_proxima_tela(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual < self.stacked_widget.count() - 1:
            proximo = index_atual + 1
            self._preparar_tela(proximo)
            self.stacked_widget.setCurrentIndex(proximo)

    def ir_para_tela_anterior(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual > 0:
            anterior = index_atual - 1
            self._preparar_tela(anterior)
            self.stacked_widget.setCurrentIndex(anterior)

    def _preparar_tela(self, index: int):
        widget = self.stacked_widget.widget(index)
        # If the target widget is any TemplateFieldsScreen, populate it with stored values
        if isinstance(widget, TemplateFieldsScreen):
            widget.set_data(self.data_model.get_template_field_values())
    
    def _coletar_dados_tela_atual(self):
        """Collect data from the currently visible screen."""
        index_atual = self.stacked_widget.currentIndex()
        widget = self.stacked_widget.currentWidget()
        
        # Screen 0: Template
        if widget is self.tela_template:
            template_path = self.tela_template.get_template_path()
            template_doc = self.tela_template.get_template_document()
            if template_path and template_doc:
                self.data_model.set_template(template_path, template_doc)
        
        # Screen 1: Patient
        elif widget is self.tela_paciente:
            patient_data = self.tela_paciente.get_data()
            if "patient" in patient_data:
                self.data_model.set_patient_data(patient_data["patient"])
            if "resp1" in patient_data:
                self.data_model.set_resp1_data(patient_data["resp1"])
            if "resp2" in patient_data:
                self.data_model.set_resp2_data(patient_data["resp2"])
            if "template_fields" in patient_data:
                self.data_model.set_template_field_values(patient_data["template_fields"])
        
        # Legacy Conclusion screen (backwards compatibility)
        elif hasattr(self, "tela_conclusao") and widget is self.tela_conclusao:
            conclusion_data = self.tela_conclusao.get_data()
            if "conclusao_text" in conclusion_data:
                self.data_model.set_conclusion_text(conclusion_data["conclusao_text"])

        # Template fields screens (administrative, clinical, behavior, conclusions)
        elif isinstance(widget, TemplateFieldsScreen):
            template_fields = widget.get_data()
            if template_fields:
                self.data_model.set_template_field_values(template_fields)

            # If this is the conclusions section, map the main free-text conclusion into the model's conclusion_text
            # Prefer field `CONCLUSAO_ANALISE_LIVRE` if present, otherwise do nothing
            if "CONCLUSAO_ANALISE_LIVRE" in template_fields:
                self.data_model.set_conclusion_text(template_fields.get("CONCLUSAO_ANALISE_LIVRE", ""))
        
        # Screen 3: Tests
        elif widget is self.tela_testes:
            test_data = self.tela_testes.get_data()
            if test_data:
                self.data_model.set_test_results(test_data)
        
        # Note: explicit ConclusionScreen removed; conclusion data now comes from conclusions section above.
    
    def _ir_para_revisao(self):
        """Navigate to review screen, collecting conclusion data first."""
        # Collect conclusion data before showing review (conclusions now live in conclusions section)
        self._coletar_dados_tela_atual()
        
        # Navigate to review screen (index of tela_revisao)
        index_revisao = self.stacked_widget.indexOf(self.tela_revisao)
        self._preparar_tela(index_revisao)
        self.stacked_widget.setCurrentIndex(index_revisao)
    
    def gerar_laudo(self):
        """Generate the final document (DOCX and PDF) with all collected data."""
        # Ensure current screen data (including conclusions section) is collected before generating
        self._coletar_dados_tela_atual()
        
        # Validate template is loaded
        if not self.data_model.is_template_loaded():
            QMessageBox.critical(
                self,
                'Erro',
                'Nenhum template foi carregado. Por favor, carregue um template antes de gerar o laudo.'
            )
            return
        
        # Initialize template processor
        processor = TemplateProcessor(self.data_model.template_document)
        
        # Extract and validate fields
        template_fields = processor.extract_fields()
        valid_fields, invalid_fields = processor.validate_fields()
        
        # Show warning if invalid fields found
        if invalid_fields:
            invalid_list = '\n'.join([f"  - {field}: {reason}" for field, reason in invalid_fields])
            reply = QMessageBox.warning(
                self,
                'Campos Inválidos Encontrados',
                f'O template contém campos que não seguem a convenção de nomenclatura:\n\n{invalid_list}\n\n'
                'Deseja continuar mesmo assim?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
        
        # Get field mapping from data model
        field_mapping = self.data_model.get_field_mapping()
        
        # Check for missing or empty fields
        missing_fields, empty_fields = processor.check_required_fields(template_fields, field_mapping)
        
        # Show warning for missing/empty fields
        if missing_fields or empty_fields:
            warning_parts = []
            if missing_fields:
                warning_parts.append(f"Campos faltando: {', '.join(missing_fields)}")
            if empty_fields:
                warning_parts.append(f"Campos vazios: {', '.join(empty_fields)}")
            
            warning_text = '\n\n'.join(warning_parts)
            reply = QMessageBox.warning(
                self,
                'Campos Incompletos',
                f'Os seguintes campos não têm dados:\n\n{warning_text}\n\n'
                'Deseja continuar mesmo assim? Os campos vazios serão deixados em branco no documento.',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
        
        # Get output directory from user
        output_dir = QFileDialog.getExistingDirectory(
            self,
            'Selecione o diretório para salvar o laudo',
            os.path.expanduser('~')
        )
        
        if not output_dir:
            return  # User cancelled
        
        try:
            # Load a fresh copy of the template document for modification
            template_copy = Document(self.data_model.template_path)
            
            # Replace fields in the copy
            processor.set_document(template_copy)
            processor.replace_fields(field_mapping, template_copy)
            
            # Generate output filename (use patient name if available, otherwise generic)
            patient_name = self.data_model.patient_data.get("patient_name", "").strip()
            if patient_name:
                # Sanitize filename
                safe_name = "".join(c for c in patient_name if c.isalnum() or c in (' ', '-', '_')).strip()
                safe_name = safe_name.replace(' ', '_')
                base_filename = f"laudo_{safe_name}"
            else:
                base_filename = "laudo"
            
            # Save DOCX
            docx_path = os.path.join(output_dir, f"{base_filename}.docx")
            processor.save_document(template_copy, docx_path)
            
            # Show success message
            QMessageBox.information(
                self,
                'Sucesso',
                f'Laudo gerado com sucesso!\n\n'
                f'DOCX: {docx_path}\n'
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                'Erro ao Gerar Laudo',
                f'Ocorreu um erro ao gerar o laudo:\n\n{str(e)}'
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())