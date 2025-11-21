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

    def fill_demo_data(self):
        """Fill the application with demo data for testing purposes."""
        demo_patient = {
            "patient_name": "João da Silva Teste",
            "patient_birth": "01/01/2015",
            "patient_crono_age": "8",
            "patient_school": "Escola Municipal de Teste",
            "patient_class": "3º Ano B"
        }
        
        demo_resp1 = {
            "resp1_name": "Maria da Silva",
            "resp1_career": "Professora",
            "resp1_education": "Superior Completo",
            "resp1_age": 35
        }
        
        demo_resp2 = {
            "resp2_name": "José da Silva",
            "resp2_career": "Engenheiro",
            "resp2_education": "Pós-Graduação",
            "resp2_age": 38
        }
        
        demo_template_fields = {
            "solicitante_nome": "Dr. Psiquiatra Exemplo",
            "solicitante_crp": "12345/SP",
            
            # Administrativo
            "cidade_paciente": "São Paulo",
            "cidade": "São Paulo",
            "data_laudo_ano": "2023",
            "solicitante_parentesco": "Mãe",
            "solicitante_acompanhamento_duracao": "6 meses",
            "psychologist_name": "Dr. Psicólogo Demo",
            "psychologist_crp": "06/12345",
            "psico_nome": "Dr. Psicólogo Demo",
            "psico_crp": "06/12345",
            "formacao_psicologo": "Especialista em Neuropsicologia",
            "email_contato_psicologo": "contato@psico.demo",
            "telefone_psicologo": "(11) 99999-9999",

            # Contexto Clínico
            "analise_paciente": "Paciente apresenta bom desenvolvimento cognitivo geral.",
            "anamnese_entrevistado": "Mãe relatou histórico de dificuldades escolares desde o início da alfabetização.",
            "constituicao_familiar": "Mora com os pais e um irmão mais novo.",
            "antecedentes_familiares": "Pai com histórico de TDAH.",
            "historico_desenvolvimento": "Desenvolvimento motor e da linguagem dentro dos marcos esperados.",
            "historico_escolar": "Dificuldades em matemática e leitura.",
            "indicacao_origem": "Encaminhado pela escola.",
            "intervencoes_queixa": "Realiza reforço escolar.",
            "queixa_sintomas_paciente": "Desatenção, agitação e dificuldade de seguir regras.",
            "temp_comp_vida": "8 anos",
            "numero_sessoes": "4 sessões",
            "medicacoes_exames": "Não faz uso de medicação.",
            "desenvolvimento_neuro": "Sem intercorrências neurológicas conhecidas.",
            "lista_instrumentos": "WISC-IV, RAVLT, BPA, Neupsilin.",
            "teste_finalidade": "Avaliação Neuropsicológica para investigação de TDAH.",
            "sono_alimentacao": "Sono agitado, alimentação seletiva.",
            "devolutiva_participantes": "Pais e escola.",
            "RELATO_TERCEIROS_FONTE": "Professora",
            "RELATO_TERCEIROS_DESC": "Relata que o aluno não para sentado.",
            "RELATO_TERCEIROS_COMPLEMENTO": "Dispersa-se facilmente com estímulos visuais.",

            # Comportamento Observado
            "ATENCAO_INICIATIVA_DESC": "Inicia tarefas mas perde o foco rapidamente.",
            "ATENCAO_RESPOSTA_DESC": "Responde bem a estímulos visuais.",
            "atencao_auditiva_conclusao": "Atenção auditiva preservada.",
            "LING_EXP_INICIATIVA": "Boa iniciativa comunicativa.",
            "LING_EXP_NIVEL": "Vocabulário adequado para a idade.",
            "LING_EXP_OBSERVACAO": "Fala fluente e articulada.",
            "LING_RECEP_HABILIDADE_COMPLEXA": "Compreende ordens complexas.",
            "LING_RECEP_HABILIDADE_SIMPLES": "Compreende ordens simples.",
            "LING_RECEP_NIVEL": "Compreensão preservada.",
            "LING_RECEP_RESPONSIVIDADE": "Responde quando chamado.",
            "LING_RECEP_ROTINA": "Segue rotinas verbais.",
            "PISTAS_SOCIAIS_DESC": "Identifica expressões faciais.",
            "CONTATO_VISUAL_DESC": "Mantém contato visual adequado.",
            "CONTATO_VISUAL_COMPLEMENTO": "Olhar direcionado ao interlocutor.",
            "SORRISO_DESC": "Sorriso social presente.",
            "LUDICO_EXPLORACAO_DESC": "Brinca de forma funcional.",
            "LUDICO_EXPLORACAO_COMPLEMENTO": "Uso adequado de objetos.",
            "PERFIL_DESENVOLTURA_SOCIAL": "Sociável e extrovertido.",
            "PERFIL_EMPATIA_FRUSTRACAO": "Baixa tolerância à frustração.",
            "LISTA_SINTOMAS_TEA_PERSONALIZADA": "Não apresenta sinais claros de TEA.",
            "LISTA_DE_ENCAMINHAMENTOS_GERADA": "Avaliação fonoaudiológica.",

            # Conclusões
            "CONCLUSAO_ANALISE_LIVRE": "Os dados sugerem quadro compatível com TDAH.",
            "CONCLUSAO_FUNCIONAMENTO_GERAL": "Funcionamento intelectual na média.",
            "FE_conclusao_geral": "Déficits em funções executivas.",
            "HIPOTESE_DIAGNOSTICA_FINAL": "F90.0 - Transtorno de Déficit de Atenção/Hiperatividade",
            "hipotese_diagnostica": "TDAH tipo combinado.",
            
            # Legacy / Fallback
            "conclusoes": "Sugere-se acompanhamento psicopedagógico e avaliação neurológica complementar."
        }
        
        # Demo test results (WISC-IV and others)
        demo_tests = {
            "ICV_WISC": 100, "IOP_WISC": 95, "IMO_WISC": 105, "IVP_WISC": 90,
            "DIGS_WISC": 10, "SNL_WISC": 11, "ARIT_WISC": 9, "SEME_WISC": 12,
            "RV_WISC": 10, "RNV_WISC": 11, "CUBE_WISC": 10, "VP_WISC": 9,
            "ALT_RAVLT": 50, "VE_RAVLT": 45, "IP_RAVLT": 40, "IR_RAVLT": 35,
            "AC_BPA": 80, "AD_BPA": 75, "AA_BPA": 85,
            "TASK_NEUP": 60,
            "SRS_ESCORE_TOTAL": 55,
            "F1_ETDAH": 40, "F2_ETDAH": 45, "F3_ETDAH": 50, "F4_ETDAH": 35,
            "CARS_PONTUACAO": 25,
            "FC_FDT": 30, "CI_FDT": 28
        }

        # Update Data Model
        self.data_model.set_patient_data(demo_patient)
        self.data_model.set_resp1_data(demo_resp1)
        self.data_model.set_resp2_data(demo_resp2)
        self.data_model.set_template_field_values(demo_template_fields)
        self.data_model.set_test_results(demo_tests)
        self.data_model.set_conclusion_text(demo_template_fields.get("conclusoes", ""))

        # Update Views
        # Patient Screen
        if hasattr(self.main_window, "patient_screen"):
            self.main_window.patient_screen.set_data({
                "patient": demo_patient,
                "resp1": demo_resp1,
                "resp2": demo_resp2,
                "template_fields": demo_template_fields
            })
            
        # Template Fields Screens
        # We need to update all instances of TemplateFieldsScreen
        # The model already has the data, so we can just call set_data on them with the full dict
        # or rely on prepare_view if we were navigating. But we want immediate update.
        for attr in ["admin_fields_screen", "clinical_context_screen", "behavior_screen", "conclusions_section_screen"]:
            screen = getattr(self.main_window, attr, None)
            if screen and isinstance(screen, TemplateFieldsScreen):
                screen.set_data(demo_template_fields)

        # Tests Screen
        if hasattr(self.main_window, "tests_screen"):
            self.main_window.tests_screen.set_data(demo_tests)
            
        # Conclusion Screen (Legacy)
        if hasattr(self.main_window, "conclusion_screen"):
            self.main_window.conclusion_screen.refresh_calculated_data()

        QMessageBox.information(self.main_window, "Sucesso", "Dados de teste preenchidos com sucesso!")

