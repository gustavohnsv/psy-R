from typing import Any, Dict, List, Optional

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QEvent

from .ui_conclusion import Ui_TelaConclusao
from app.models import LaudoDataModel


TEST_SUMMARY_LAYOUT: List[Dict[str, Any]] = [
    {
        "title": "WISC-IV",
        "metrics": [
            {"label": "QI Total (QIT)", "raw": "QIT_WISC", "class": "QIT_out", "text": "QIT_conclusao"},
            {"label": "Indice de Comprensao Verbal (ICV)", "raw": "ICV_WISC", "class": "ICV_out", "text": "ICV_text_out"},
            {"label": "Indice de Organizacao Perceptual (IOP)", "raw": "IOP_WISC", "class": "IOP_out", "text": "IOP_text_out"},
            {"label": "Indice de Memoria Operacional (IMO)", "raw": "IMO_WISC", "class": "IMO_out", "text": "IMO_text_out"},
            {"label": "Indice de Velocidade de Processamento (IVP)", "raw": "IVP_WISC", "class": "IVP_out", "text": "IVP_text_out"},
            {"label": "Dígitos", "raw": "DIGS_WISC", "class": "DIGS_out"},
            {"label": "Sequência N/L", "raw": "SNL_WISC", "class": "SNL_out"},
            {"label": "Aritmética", "raw": "ARIT_WISC", "class": "ARIT_out"},
            {"label": "Semelhanças", "raw": "SEME_WISC", "class": "SEME_out"},
            {"label": "Raciocínio Verbal", "raw": "RV_WISC", "class": "RV_out"},
            {"label": "Raciocínio não verbal", "raw": "RNV_WISC", "class": "RNV_out"},
            {"label": "Cubos", "raw": "CUBE_WISC", "class": "CUBE_out"},
            {"label": "Velocidade de Processamento", "raw": "VP_WISC", "class": "VP_out"},
        ],
    },
    {
        "title": "BPA-2",
        "metrics": [
            {"label": "Atencao Concentrada", "raw": "AC_BPA", "class": "AC_out"},
            {"label": "Atencao Dividida", "raw": "AD_BPA", "class": "AD_out"},
            {"label": "Atencao Alternada", "raw": "AA_BPA", "class": "AA_out"},
            {"label": "Atencao Geral", "raw": "AG_BPA", "class": "AG_out", "text": "AG_conclusao"},
        ],
    },
    {
        "title": "RAVLT",
        "metrics": [
            {"label": "Indice de Aprendizagem (IP)", "raw": "IP_RAVLT", "class": "IP_out"},
            {"label": "Indice de Retencao (IR)", "raw": "IR_RAVLT", "class": "IR_out"},
            {"label": "Velocidade de Esquecimento (VE)", "raw": "VE_RAVLT", "class": "VE_out"},
            {"label": "Estrategia de Tenta Memoria (ETM)", "raw": "ETM_RAVLT", "class": "ETM_out"},
            {"label": "Aprendizagem Tardia (ALT)", "raw": "ALT_RAVLT", "class": "ALT_out"},
        ],
    },
    {
        "title": "SRS-2",
        "metrics": [
            {"label": "Escore Total", "raw": "SRS_ESCORE_TOTAL", "class": "SRS_ESCORE_T_FAIXA"},
            {"label": "Nivel de Gravidade", "raw": None, "class": "SRS_NIVEL"},
        ],
    },
    {
        "title": "ETDAH",
        "metrics": [
            {"label": "Fator 1", "raw": "F1_ETDAH", "class": "F1_out"},
            {"label": "Fator 2", "raw": "F2_ETDAH", "class": "F2_out"},
            {"label": "Fator 3", "raw": "F3_ETDAH", "class": "F3_out"},
            {"label": "Fator 4", "raw": "F4_ETDAH", "class": "F4_out"},
            {"label": "Total", "raw": "TOTAL_ETDAH", "class": "TOTAL_out"},
        ],
    },
    {
        "title": "CARS",
        "metrics": [
            {"label": "Pontuacao Total", "raw": "CARS_PONTUACAO", "class": "CARS_INTERPRETACAO"},
        ],
    },
    {
        "title": "FDT",
        "metrics": [
            {"label": "Controle Inibitorio", "raw": "CI_FDT", "class": "CI_out"},
            {"label": "Flexibilidade Cognitiva", "raw": "FC_FDT", "class": "FC_out"},
        ],
    },
    {
        "title": "Neupsilin",
        "metrics": [
            {"label": "Desempenho", "raw": "TASK_NEUP", "class": "TASK_out"},
        ],
    },
]


class ConclusionScreen(QWidget):
    avancar_clicado = Signal()
    voltar_clicado = Signal()

    def __init__(self, parent: Optional[QWidget] = None, *, data_model: Optional[LaudoDataModel] = None):
        super().__init__(parent)
        self.ui = Ui_TelaConclusao()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)
        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)

        self._data_model: Optional[LaudoDataModel] = None
        if data_model is not None:
            self.set_data_model(data_model)

    def set_data_model(self, data_model: LaudoDataModel) -> None:
        self._data_model = data_model
        self.refresh_calculated_data()

    def refresh_calculated_data(self) -> None:
        summary = self._build_summary_text()
        if summary:
            self.ui.textBrowser_dados.setPlainText(summary)
        else:
            self.ui.textBrowser_dados.setPlainText("Nenhum dado de teste registrado.")

    def showEvent(self, event: QEvent) -> None:
        self.refresh_calculated_data()
        super().showEvent(event)
    
    def get_data(self) -> Dict[str, str]:
        """Get conclusion text data."""
        return {
            "conclusao_text": self.ui.textEdit_conclusao.toPlainText()
        }

    def _build_summary_text(self) -> str:
        if not self._data_model or not self._data_model.test_results:
            return ""

        results = self._data_model.test_results
        lines: List[str] = []

        for section in TEST_SUMMARY_LAYOUT:
            section_lines: List[str] = []
            for metric in section.get("metrics", []):
                raw_key = metric.get("raw")
                class_key = metric.get("class")
                text_key = metric.get("text")

                raw_value = results.get(raw_key) if raw_key else None
                class_value = results.get(class_key) if class_key else None
                text_value = results.get(text_key) if text_key else None

                if raw_value is None and class_value is None and not text_value:
                    continue

                display_raw = self._format_value(raw_value) if raw_key else "-"
                entry = f"- {metric['label']}: {display_raw}"

                if class_value is not None:
                    entry = f"{entry} | {self._format_value(class_value)}"

                section_lines.append(entry)

                if text_value:
                    section_lines.append(f"    {self._normalize_whitespace(text_value)}")

            if section_lines:
                lines.append(section["title"])
                lines.extend(section_lines)
                lines.append("")

        if not lines:
            fallback = ["Resultados registrados:"]
            for key in sorted(results.keys()):
                fallback.append(f"- {key}: {self._format_value(results.get(key))}")
            return "\n".join(fallback)

        return "\n".join(line.rstrip() for line in lines).strip()

    @staticmethod
    def _format_value(value: Any) -> str:
        if value is None:
            return "-"
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    @staticmethod
    def _normalize_whitespace(text: Any) -> str:
        if not isinstance(text, str):
            return str(text)
        return " ".join(text.split())