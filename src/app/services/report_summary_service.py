from typing import Dict, Any, Optional

class ReportSummaryService:
    """Service responsible for generating report summaries from test results."""
    
    # Layout configuration for the summary
    TEST_SUMMARY_LAYOUT = {
        "Atenção": [
            ("BPA", "Atenção Concentrada", "AC_percentil", "AC_classificacao"),
            ("BPA", "Atenção Dividida", "AD_percentil", "AD_classificacao"),
            ("BPA", "Atenção Alternada", "AA_percentil", "AA_classificacao"),
            ("BPA", "Atenção Geral", "AG_percentil", "AG_classificacao"),
        ],
        "Memória": [
            ("MVR", "Memória Visual (Rosto)", "MVR_percentil", "MVR_classificacao"),
            ("TEPIC-M", "Memória Visual (Figuras)", "TEPIC_M_percentil", "TEPIC_M_classificacao"),
        ],
        "Inteligência": [
            ("R-1", "Inteligência Não Verbal", "R1_percentil", "R1_classificacao"),
            ("G-36", "Inteligência Geral", "G36_percentil", "G36_classificacao"),
            ("Raven", "Matrizes Progressivas", "Raven_percentil", "Raven_classificacao"),
        ],
        "Personalidade": [
            ("Quati", "Personalidade", None, "Quati_classificacao"),
            ("Palográfico", "Produtividade", "Palo_produtividade_percentil", "Palo_produtividade_classificacao"),
        ]
    }

    def build_summary_text(self, test_results: Dict[str, Any]) -> str:
        """Build a formatted summary text from test results."""
        lines = []
        
        for category, items in self.TEST_SUMMARY_LAYOUT.items():
            category_lines = []
            for test_name, label, perc_key, class_key in items:
                # Check if we have data for this item
                # We look for keys in test_results that match the pattern
                # Usually keys are like "AC_percentil" directly in the flat dict
                
                percentil = test_results.get(perc_key) if perc_key else None
                classificacao = test_results.get(class_key)
                
                # Special handling for Quati which has no percentile
                if test_name == "Quati":
                    if classificacao:
                        category_lines.append(f"- {test_name} ({label}): {classificacao}")
                    continue
                
                # For others, we need at least classification or percentile
                if percentil or classificacao:
                    text = f"- {test_name} ({label}):"
                    if percentil:
                        text += f" Percentil {percentil}"
                    if classificacao:
                        text += f" - {classificacao}"
                    category_lines.append(text)
            
            if category_lines:
                lines.append(f"=== {category} ===")
                lines.extend(category_lines)
                lines.append("")  # Empty line after category
        
        return "\n".join(lines).strip()
