import re
from typing import List, Tuple, Set


class FieldValidator:
    """Validates field names against the program's naming convention."""
    
    # Define valid field name patterns - more permissive to accept actual template fields
    PATTERNS = {
        # Patient fields - accepts both patient_* and nome_paciente, data_nasc_paciente, etc.
        'patient_standard': re.compile(r'^patient_(name|birth|crono_age|school|class)$'),
        'patient_alternative': re.compile(r'^(nome|data_nasc|escola|turma|cidade|idd|primeiro_nome|historico_escolar|historico_desenvolvimento|desenvolvimento_neuro|constituicao_familiar|sono_alimentacao|antecedentes_familiares|queixa_sintomas|analise|temp_comp_vida|indicacao_origem|teste_finalidade|numero_sessoes|medicacoes_exames|intervencoes_queixa|anamnese_entrevistado|devolutiva_participantes|hipotese_diagnostica|atencao_auditiva_conclusao|FE_conclusao_geral|lista_instrumentos|data_laudo_ano)_paciente$'),
        
        # Respondent fields - accepts resp1/resp2 with various field names
        'resp1': re.compile(r'^resp1_(nome|name|profissao|career|escolaridade|education|idade|age)$'),
        'resp2': re.compile(r'^resp2_(nome|name|profissao|career|escolaridade|education|idade|age)$'),
        
        # Psychologist fields - accepts various psychologist field patterns
        'psychologist_standard': re.compile(r'^(psychologist_name|psychologist_crp|nome_psicologo|crp_psicologo)$'),
        'psychologist_alternative': re.compile(r'^(psico_nome|psico_crp|telefone_psicologo|formacao_psicologo|email_contato_psicologo|solicitante_nome|solicitante_crp|solicitante_parentesco|solicitante_acompanhamento_duracao)$'),
        
        # Conclusion fields
        'conclusion': re.compile(r'^(conclusion_text|conclusao.*)$'),
        
        # Test fields - WISC patterns (accepts _WISC suffix and various output patterns)
        'test_wisc': re.compile(r'^(QIT|ICV|IOP|IMO|IVP|ARIT|DIGS|SNL|SEME|CUBE|RV|RNV|VP|FC|CI|TASK|SEM|INF|VOC|COM|AG|AA|AC|AD|IR|IP|VE|ETM|ALT)(_WISC|_out|_conclusao|_text_out|_compostos|_percentil|_habilidade_descritiva|_HL)?$'),
        
        # Test fields - ETDAH patterns
        'test_etdah': re.compile(r'^(F1|F2|F3|F4|TOTAL|ETDAH)(_ETDAH|_ETADH|_out|_CONCLUSAO_BLOCO)?$'),
        
        # Test fields - RAVLT patterns
        'test_ravlt': re.compile(r'^(IP|IR|VE|ETM|ALT|RAVLT)(_RAVLT|_out|_ANALISE_PERFIL)?$'),
        
        # Test fields - Other tests (CARS, SRS, BPA, FDT, HTP, NEUPSILIN)
        'test_cars': re.compile(r'^CARS(_PONTUACAO|_INTERPRETACAO)?$'),
        'test_srs': re.compile(r'^SRS(_ESCORE_TOTAL|_ESCORE_T_FAIXA|_NIVEL|_INTERPRETACAO_BLOCO)?$'),
        'test_bpa': re.compile(r'^(AG|AA|AC|AD)(_BPA|_out|_pontuacao|_conclusao)?$'),
        'test_fdt': re.compile(r'^(CI|FC)(_FDT|_out|_habilidade_descritiva)?$'),
        'test_htp': re.compile(r'^HTP(_CONECTOR|_AMBIENTE_INFERENCIA|_PROJECAO_COMPLEMENTO|_PROJECAO_DESC|_CONCLUSAO_ANALISE|_ASPECTOS_FORMAIS_DESC)?$'),
        'test_neupsilin': re.compile(r'^(TASK|PLAN|VP|FC|CI|RV)(_NEUP|_out|_habilidade_descritiva)?$'),
        
        # Language and communication fields
        'language': re.compile(r'^LING_(EXP|RECEP)(_OBSERVACAO|_NIVEL|_INICIATIVA|_RESPONSIVIDADE|_HABILIDADE_(SIMPLES|COMPLEXA)|_ROTINA)?$'),
        
        # Theory of Mind fields
        'theory_of_mind': re.compile(r'^TOM_(INFERENCIA_DESC|CONTEXTO_DESC|EXPRESSOES_(SIMPLES|COMPLEXAS)_DESC)$'),
        
        # Social and behavioral fields
        'social_behavioral': re.compile(r'^(CONTATO_VISUAL|SORRISO|PISTAS_SOCIAIS|ATENCAO_(INICIATIVA|RESPOSTA)|LUDICO_EXPLORACAO|RELATO_TERCEIROS|PERFIL_(EMPATIA_FRUSTRACAO|DESENVOLTURA_SOCIAL))(_DESC|_COMPLEMENTO|_FONTE)?$'),
        
        # Visual and memory fields
        'visual_memory': re.compile(r'^VISUO_(MEM|COPIA)(_HABILIDADE_DESC|_OBSERVACAO|_CLASSIFICACAO|_INTERPRETACAO)?$'),
        
        # Conclusion and diagnostic fields
        'conclusion_diagnostic': re.compile(r'^(CONCLUSAO|HIPOTESE_DIAGNOSTICA|LISTA)(_FUNCIONAMENTO_GERAL|_ANALISE_LIVRE|_ADAPTATIVA|_FINAL|_DE_ENCAMINHAMENTOS_GERADA|_SINTOMAS_TEA_PERSONALIZADA)?$'),
        
        # Generic uppercase test fields (any uppercase field with underscores)
        'test_generic_uppercase': re.compile(r'^[A-Z][A-Z0-9_]+$'),
        
        # Generic lowercase descriptive fields (any lowercase field with underscores)
        'generic_lowercase': re.compile(r'^[a-z][a-z0-9_]+$'),
    }
    
    @classmethod
    def validate_field_name(cls, field_name: str) -> Tuple[bool, str]:
        """Validate a single field name against naming convention.
        
        Args:
            field_name: The field name to validate (without braces)
            
        Returns:
            Tuple of (is_valid, reason)
        """
        # Basic validation: field must be alphanumeric with underscores, not empty
        if not field_name or not re.match(r'^[a-zA-Z0-9_]+$', field_name):
            return False, f"Field '{field_name}' contains invalid characters"
        
        # Check against all patterns
        for pattern_name, pattern in cls.PATTERNS.items():
            if pattern.match(field_name):
                return True, f"Valid {pattern_name} field"
        
        # If no specific pattern matches but it's a valid format, accept it
        # This allows for flexibility with template fields
        if re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', field_name):
            return True, "Valid field name format"
        
        # If no pattern matches, it's invalid
        return False, f"Field '{field_name}' does not follow naming convention"
    
    @classmethod
    def validate_fields(cls, field_names: List[str]) -> Tuple[List[str], List[Tuple[str, str]]]:
        """Validate a list of field names.
        
        Args:
            field_names: List of field names to validate (without braces)
            
        Returns:
            Tuple of (valid_fields, invalid_fields_with_reasons)
            invalid_fields_with_reasons is a list of (field_name, reason) tuples
        """
        valid_fields = []
        invalid_fields = []
        
        for field_name in field_names:
            is_valid, reason = cls.validate_field_name(field_name)
            if is_valid:
                valid_fields.append(field_name)
            else:
                invalid_fields.append((field_name, reason))
        
        return valid_fields, invalid_fields
    
    @classmethod
    def get_expected_field_categories(cls) -> dict:
        """Get a dictionary of expected field categories and examples."""
        return {
            'patient': ['patient_name', 'patient_birth', 'patient_crono_age', 'patient_school', 'patient_class'],
            'respondent_1': ['resp1_name', 'resp1_career', 'resp1_education', 'resp1_age'],
            'respondent_2': ['resp2_name', 'resp2_career', 'resp2_education', 'resp2_age'],
            'psychologist': ['psychologist_name', 'psychologist_crp', 'nome_psicologo', 'crp_psicologo'],
            'conclusion': ['conclusion_text', 'conclusao_text'],
            'test_wisc': ['QIT_out', 'ICV_out', 'IOP_out', 'QIT_conclusao', 'ICV_text_out'],
            'test_etdah': ['F1_out', 'F2_out', 'F3_out', 'F4_out', 'TOTAL_out', 'ETDAH_CONCLUSAO_BLOCO'],
            'test_generic': ['Any uppercase field ending with _out, _conclusao, or _text_out']
        }

