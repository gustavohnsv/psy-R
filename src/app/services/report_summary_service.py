from typing import Dict, Any, Optional

class ReportSummaryService:
    """Service responsible for generating report summaries from test results."""
    
    def build_summary_text(self, test_results: Dict[str, Any]) -> str:
        """Build a formatted summary text from test results."""
        lines = []
        
        # --- WISC-IV ---
        wisc_lines = []
        wisc_map = [
            ("QIT", "QI Total", "QIT_WISC", "QIT_out", "QIT_conclusao"),
            ("ICV", "Índice de Compreensão Verbal", "ICV_WISC", "ICV_out", "ICV_text_out"),
            ("IOP", "Índice de Organização Perceptual", "IOP_WISC", "IOP_out", "IOP_text_out"),
            ("IMO", "Índice de Memória Operacional", "IMO_WISC", "IMO_out", "IMO_text_out"),
            ("IVP", "Índice de Velocidade de Processamento", "IVP_WISC", "IVP_out", "IVP_text_out"),
        ]
        
        for prefix, label, score_key, class_key, text_key in wisc_map:
            score = test_results.get(score_key)
            classification = test_results.get(class_key)
            text = test_results.get(text_key)
            
            if score is not None or classification:
                line = f"- {label} ({prefix}):"
                if score is not None:
                    line += f" {score}"
                if classification:
                    line += f" | {classification}"
                wisc_lines.append(line)
                
                if text:
                    # Indent description
                    wisc_lines.append(f"  {text}")

        # WISC Subtests (Optional, if desired in summary)
        wisc_sub_map = [
            ("DIGS", "Dígitos", "DIGS_WISC", "DIGS_out"),
            ("SNL", "Sequência N/L", "SNL_WISC", "SNL_out"),
            ("ARIT", "Aritmética", "ARIT_WISC", "ARIT_out"),
            ("SEME", "Semelhanças", "SEME_WISC", "SEME_out"),
            ("RV", "Raciocínio Verbal", "RV_WISC", "RV_out"),
            ("RNV", "Raciocínio Não Verbal", "RNV_WISC", "RNV_out"),
            ("CUBE", "Cubos", "CUBE_WISC", "CUBE_out"),
            ("VP", "Velocidade de Processamento", "VP_WISC", "VP_out"),
        ]
        
        for prefix, label, score_key, class_key in wisc_sub_map:
             score = test_results.get(score_key)
             classification = test_results.get(class_key)
             if score is not None or classification:
                line = f"- {label}:"
                if score is not None:
                    line += f" {score}"
                if classification:
                    line += f" | {classification}"
                wisc_lines.append(line)

        if wisc_lines:
            lines.append("WISC-IV")
            lines.extend(wisc_lines)
            lines.append("")

        # --- RAVLT ---
        ravlt_lines = []
        ravlt_map = [
            ("ALT", "Aprendizagem", "ALT_RAVLT", "ALT_out"),
            ("VE", "Velocidade de Esquecimento", "VE_RAVLT", "VE_out"),
            ("IP", "Interferência Proativa", "IP_RAVLT", "IP_out"),
            ("IR", "Interferência Retroativa", "IR_RAVLT", "IR_out"),
        ]
        
        for prefix, label, score_key, class_key in ravlt_map:
            score = test_results.get(score_key)
            classification = test_results.get(class_key)
            if score is not None or classification:
                line = f"- {label}:"
                if score is not None:
                    line += f" {score}"
                if classification:
                    line += f" | {classification}"
                ravlt_lines.append(line)
                
        if ravlt_lines:
            lines.append("RAVLT")
            lines.extend(ravlt_lines)
            lines.append("")

        # --- BPA ---
        bpa_lines = []
        bpa_map = [
            ("AC", "Atenção Concentrada", "AC_BPA", "AC_out"),
            ("AD", "Atenção Dividida", "AD_BPA", "AD_out"),
            ("AA", "Atenção Alternada", "AA_BPA", "AA_out"),
            ("AG", "Atenção Geral", "AG_BPA", "AG_out"),
        ]
        
        for prefix, label, score_key, class_key in bpa_map:
            score = test_results.get(score_key)
            classification = test_results.get(class_key)
            if score is not None or classification:
                line = f"- {label}:"
                if score is not None:
                    line += f" {score}"
                if classification:
                    line += f" | {classification}"
                bpa_lines.append(line)

        if bpa_lines:
            lines.append("BPA")
            lines.extend(bpa_lines)
            lines.append("")

        # --- Neupsilin ---
        neup_lines = []
        task_score = test_results.get("TASK_NEUP")
        task_out = test_results.get("TASK_out")
        if task_score is not None or task_out:
            line = "- Tarefas:"
            if task_score is not None:
                line += f" {task_score}"
            if task_out:
                line += f" | {task_out}"
            neup_lines.append(line)
            
        if neup_lines:
            lines.append("Neupsilin")
            lines.extend(neup_lines)
            lines.append("")

        # --- SRS-2 ---
        srs_lines = []
        srs_nivel = test_results.get("SRS_NIVEL")
        if srs_nivel:
            srs_lines.append(f"- Classificação: {srs_nivel}")
            
        if srs_lines:
            lines.append("SRS-2")
            lines.extend(srs_lines)
            lines.append("")

        # --- CARS ---
        cars_lines = []
        cars_interp = test_results.get("CARS_INTERPRETACAO")
        if cars_interp:
            cars_lines.append(f"- Interpretação: {cars_interp}")
            
        if cars_lines:
            lines.append("CARS")
            lines.extend(cars_lines)
            lines.append("")

        # --- ETDAH ---
        etdah_lines = []
        etdah_map = [
            ("F1", "Regulação Emocional", "F1_ETDAH", "F1_out"),
            ("F2", "Autorregulação", "F2_ETDAH", "F2_out"),
            ("F3", "Flexibilidade", "F3_ETDAH", "F3_out"),
            ("F4", "Atenção", "F4_ETDAH", "F4_out"),
        ]
        
        for prefix, label, score_key, class_key in etdah_map:
            score = test_results.get(score_key)
            classification = test_results.get(class_key)
            if score is not None or classification:
                line = f"- {label}:"
                if score is not None:
                    line += f" {score}"
                if classification:
                    line += f" | {classification}"
                etdah_lines.append(line)

        if etdah_lines:
            lines.append("ETDAH")
            lines.extend(etdah_lines)
            lines.append("")

        return "\n".join(lines).strip()
