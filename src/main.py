import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QFileDialog, QMessageBox
from docx import Document

from app.views import (
    TemplateScreen,
    PatientScreen,
    TestsScreen,
    ConclusionScreen,
    ReviewScreen
)
from app.models import LaudoDataModel
from app.services import TemplateProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente de Laudo Psicológico")
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
        self.tela_testes = TestsScreen()
        self.tela_conclusao = ConclusionScreen()
        self.tela_revisao = ReviewScreen(data_model=self.data_model)

        self.stacked_widget.addWidget(self.tela_template)
        self.stacked_widget.addWidget(self.tela_paciente)
        self.stacked_widget.addWidget(self.tela_testes)
        self.stacked_widget.addWidget(self.tela_conclusao)
        self.stacked_widget.addWidget(self.tela_revisao)

        self.tela_template.avancar_clicado.connect(self.ir_para_proxima_tela)

        self.tela_paciente.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_paciente.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_testes.avancar_clicado.connect(self.ir_para_proxima_tela)
        self.tela_testes.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_conclusao.avancar_clicado.connect(self._ir_para_revisao)
        self.tela_conclusao.voltar_clicado.connect(self.ir_para_tela_anterior)

        self.tela_revisao.voltar_clicado.connect(self.ir_para_tela_anterior)
        self.tela_revisao.gerar_laudo_clicado.connect(self.gerar_laudo)

    def ir_para_proxima_tela(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index_atual + 1)

    def ir_para_tela_anterior(self):
        # Collect data from current screen before navigating
        self._coletar_dados_tela_atual()
        
        index_atual = self.stacked_widget.currentIndex()
        if index_atual > 0:
            self.stacked_widget.setCurrentIndex(index_atual - 1)
    
    def _coletar_dados_tela_atual(self):
        """Collect data from the currently visible screen."""
        index_atual = self.stacked_widget.currentIndex()
        
        # Screen 0: Template
        if index_atual == 0:
            template_path = self.tela_template.get_template_path()
            template_doc = self.tela_template.get_template_document()
            if template_path and template_doc:
                self.data_model.set_template(template_path, template_doc)
        
        # Screen 1: Patient
        elif index_atual == 1:
            patient_data = self.tela_paciente.get_data()
            if "patient" in patient_data:
                self.data_model.set_patient_data(patient_data["patient"])
            if "resp1" in patient_data:
                self.data_model.set_resp1_data(patient_data["resp1"])
            if "resp2" in patient_data:
                self.data_model.set_resp2_data(patient_data["resp2"])
        
        # Screen 2: Tests
        elif index_atual == 2:
            test_data = self.tela_testes.get_data()
            if test_data:
                self.data_model.set_test_results(test_data)
        
        # Screen 3: Conclusion
        elif index_atual == 3:
            conclusion_data = self.tela_conclusao.get_data()
            if "conclusao_text" in conclusion_data:
                self.data_model.set_conclusion_text(conclusion_data["conclusao_text"])
    
    def _ir_para_revisao(self):
        """Navigate to review screen, collecting conclusion data first."""
        # Collect conclusion data before showing review
        conclusion_data = self.tela_conclusao.get_data()
        if "conclusao_text" in conclusion_data:
            self.data_model.set_conclusion_text(conclusion_data["conclusao_text"])
        
        # Navigate to review screen (index 4)
        self.stacked_widget.setCurrentIndex(4)
    
    def gerar_laudo(self):
        """Generate the final document (DOCX and PDF) with all collected data."""
        # Collect data from conclusion screen one more time
        conclusion_data = self.tela_conclusao.get_data()
        if "conclusao_text" in conclusion_data:
            self.data_model.set_conclusion_text(conclusion_data["conclusao_text"])
        
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
            
            # Convert to PDF
            pdf_path = os.path.join(output_dir, f"{base_filename}.pdf")
            processor.convert_to_pdf(docx_path, pdf_path)
            
            # Show success message
            QMessageBox.information(
                self,
                'Sucesso',
                f'Laudo gerado com sucesso!\n\n'
                f'DOCX: {docx_path}\n'
                f'PDF: {pdf_path}'
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