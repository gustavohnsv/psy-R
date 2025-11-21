"""Classification helpers for psychological test results."""
from __future__ import annotations

from typing import Any, Dict, Optional, Iterable, Callable, List

from .test_tables_loader import TestTablesLoader


class TestResultClassifier:
    """Apply interval-based classifications to raw test scores.

    The classifier reads JSON tables from ``src/app/data`` via ``TestTablesLoader``
    and exposes a single method, :meth:`classify_results`, that augments a raw
    result mapping with human-readable interpretation strings expected by the
    DOCX templates (e.g. ``QIT_out``).
    """

    def __init__(self, loader: Optional[TestTablesLoader] = None):
        self._loader = loader or TestTablesLoader()
        self._tables = self._loader.load_all()

    # Public API -----------------------------------------------------------------
    def classify_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Return ``results`` plus any derived classification fields."""
        if not isinstance(results, dict) or not results:
            return results

        augmented = dict(results)

        self._apply_wisc(augmented, results)
        self._apply_ravlt(augmented, results)
        self._apply_bpa(augmented, results)
        self._apply_fdt(augmented, results)
        self._apply_srs(augmented, results)
        self._apply_etdah(augmented, results)
        self._apply_cars(augmented, results)
        self._apply_neupsilin(augmented, results)

        return augmented

    # Helpers --------------------------------------------------------------------
    def _apply_wisc(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "wisc"
        if table_key not in self._tables:
            return

        prefixes = ("QIT", "ICV", "IOP", "IMO", "IVP")
        scores: Dict[str, Optional[float]] = {
            prefix: self._to_number(source.get(f"{prefix}_WISC"))
            for prefix in prefixes
        }

        if scores.get("QIT") is None:
            components = [scores[p] for p in ("ICV", "IOP", "IMO", "IVP") if scores.get(p) is not None]
            if components:
                scores["QIT"] = sum(components) / len(components)
                if "QIT_WISC" not in target:
                    target["QIT_WISC"] = int(round(scores["QIT"]))

        for prefix in prefixes:
            score = scores.get(prefix)
            if score is None:
                continue

            classification = self._classify_value(
                table_key,
                score,
                classification_key="classificacoes_pp",
                postprocess=self._strip_pontuacao_prefix,
            )
            if classification is None:
                continue

            self._store_if_empty(target, f"{prefix}_out", classification)

            descriptive = self._build_wisc_text(prefix, classification)
            if descriptive:
                field_name = "QIT_conclusao" if prefix == "QIT" else f"{prefix}_text_out"
                self._store_if_empty(target, field_name, descriptive)

        subtests = {
            "DIGS_WISC": "DIGS_out",
            "SNL_WISC": "SNL_out",
            "ARIT_WISC": "ARIT_out",
            "SEME_WISC": "SEME_out",
            "RV_WISC": "RV_out",
            "RNV_WISC": "RNV_out",
            "CUBE_WISC": "CUBE_out",
            "VP_WISC": "VP_out",
        }

        for raw_field, out_field in subtests.items():
            raw_score = self._to_number(source.get(raw_field))
            if raw_score is None:
                continue

            classification = self._classify_value(
                table_key,
                raw_score,
                classification_key="classificacoes_pp",
                postprocess=self._strip_pontuacao_prefix,
            )

            if classification is None:
                continue

            self._store_if_empty(target, out_field, classification)

    def _apply_ravlt(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "ravlt"
        if table_key not in self._tables:
            return

        prefixes = ("IP", "IR", "VE", "ETM", "ALT")
        for prefix in prefixes:
            percentile = self._to_number(source.get(f"{prefix}_RAVLT"))
            if percentile is None:
                continue
            classification = self._classify_value(table_key, percentile)
            if classification is None:
                continue
            self._store_if_empty(target, f"{prefix}_out", classification)

    def _apply_bpa(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "bpa"
        if table_key not in self._tables:
            return

        mapping = {
            "AG_BPA": "AG_conclusao",
            "AA_BPA": "AA_out",
            "AC_BPA": "AC_out",
            "AD_BPA": "AD_out",
        }

        values = dict(source)
        raw_general = self._to_number(values.get("AG_BPA"))
        generated_general = False
        if raw_general is None:
            components = [
                self._to_number(values.get(key))
                for key in ("AC_BPA", "AD_BPA", "AA_BPA")
            ]
            components = [value for value in components if value is not None]
            if components:
                raw_general = sum(components) / len(components)
                values["AG_BPA"] = raw_general
                generated_general = True

        for raw_field, result_field in mapping.items():
            raw_value = values.get(raw_field)
            percentile = self._to_number(raw_value)
            if percentile is None:
                continue
            classification = self._classify_value(table_key, percentile)
            if classification is None:
                continue
            self._store_if_empty(target, result_field, classification)
            if raw_field == "AG_BPA":
                self._store_if_empty(target, "AG_out", classification)
                if generated_general and "AG_BPA" not in target:
                    target["AG_BPA"] = int(round(percentile))
                if raw_value is not None and "AG_pontuacao" not in target:
                    formatted = int(round(percentile)) if isinstance(percentile, float) else raw_value
                    target["AG_pontuacao"] = formatted

    def _apply_fdt(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "fdt"
        if table_key not in self._tables:
            return

        mapping = {
            "CI_FDT": "CI_out",
            "FC_FDT": "FC_out",
        }

        for raw_field, result_field in mapping.items():
            percentile = self._to_number(source.get(raw_field))
            if percentile is None:
                continue
            classification = self._classify_value(table_key, percentile)
            if classification is None:
                continue
            self._store_if_empty(target, result_field, classification)

    def _apply_srs(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "srs"
        if table_key not in self._tables:
            return

        raw_score = self._to_number(source.get("SRS_ESCORE_TOTAL"))
        if raw_score is None:
            return

        classification = self._classify_value(table_key, raw_score)
        if classification is None:
            return

        # Store short version
        self._store_if_empty(target, "SRS_ESCORE_T_FAIXA", classification)

        interpretation = self._classify_value(table_key, raw_score, text_key="interpretacao")
        
        if interpretation:
            combined = f"{classification}: {interpretation}"
            self._store_if_empty(target, "SRS_NIVEL", combined)
            self._store_if_empty(target, "SRS_INTERPRETACAO", interpretation)
        else:
            self._store_if_empty(target, "SRS_NIVEL", classification)

    def _apply_etdah(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "etdah"
        if table_key not in self._tables:
            return

        prefixes = ("F1", "F2", "F3", "F4", "TOTAL")
        for prefix in prefixes:
            raw_value = source.get(f"{prefix}_ETDAH")
            if raw_value is None and prefix == "TOTAL":
                # alguns templates usam ETADH por engano
                raw_value = source.get("TOTAL_ETADH")
            percentile = self._to_number(raw_value)
            if percentile is None:
                continue
            classification = self._classify_value(table_key, percentile)
            if classification is None:
                continue
            self._store_if_empty(target, f"{prefix}_out", classification)

    def _apply_cars(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "cars"
        if table_key not in self._tables:
            return

        raw_score = self._to_number(source.get("CARS_PONTUACAO"))
        if raw_score is None:
            return

        classification = self._classify_value(table_key, raw_score, text_key="interpretacao")
        if classification is None:
            return
        self._store_if_empty(target, "CARS_INTERPRETACAO", classification)

    def _apply_neupsilin(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        table_key = "neupsilin"
        if table_key not in self._tables:
            return

        percentile = self._to_number(source.get("TASK_NEUP"))
        if percentile is None:
            return
        classification = self._classify_value(table_key, percentile)
        if classification is None:
            return
        self._store_if_empty(target, "TASK_out", classification)

    # Low-level utilities --------------------------------------------------------
    def _classify_value(
        self,
        table_key: str,
        value: float,
        *,
        classification_key: Optional[str] = None,
        text_key: Optional[str] = None,
        postprocess: Optional[Callable[[str], str]] = None,
    ) -> Optional[str]:
        table = self._tables.get(table_key)
        if not table:
            return None

        rules: Iterable[Dict[str, Any]]
        if classification_key and table.get(classification_key):
            rules = table[classification_key]  # type: ignore[assignment]
        elif table.get("classificacoes"):
            rules = table["classificacoes"]  # type: ignore[assignment]
        else:
            return None

        rules_list = list(rules)
        if not rules_list:
            return None

        bounds: List[tuple[float, float]] = []
        for rule in rules_list:
            try:
                min_value = float(rule.get("faixa_min"))
                max_value = float(rule.get("faixa_max"))
            except (TypeError, ValueError):
                continue
            bounds.append((min_value, max_value))

        if bounds:
            global_min = min(item[0] for item in bounds)
            global_max = max(item[1] for item in bounds)
            value = max(global_min, min(global_max, value))

        chosen: Optional[str] = None
        for rule in rules_list:
            try:
                min_value = float(rule.get("faixa_min"))
                max_value = float(rule.get("faixa_max"))
            except (TypeError, ValueError):
                continue
            if min_value <= value <= max_value:
                key = text_key or "texto"
                text = rule.get(key)
                if not text and key != "interpretacao":
                    text = rule.get("interpretacao")
                if isinstance(text, str):
                    chosen = text
                break

        if chosen and postprocess:
            chosen = postprocess(chosen)

        return chosen

    @staticmethod
    def _strip_pontuacao_prefix(text: str) -> str:
        lowered = text.lower()
        prefix = "pontuação "
        if lowered.startswith(prefix):
            text = text[len(prefix):]
        return text[:1].upper() + text[1:] if text else text

    def _build_wisc_text(self, prefix: str, classification: str) -> Optional[str]:
        table = self._tables.get("wisc")
        if not isinstance(table, dict):
            return None

        options = table.get("opcoes_texto_analise")
        if not isinstance(options, dict):
            return None

        option_key = {
            "QIT": "QIT_conclusao",
            "ICV": "ICV_text_out",
            "IOP": "IOP_text_out",
            "IMO": "IMO_text_out",
            "IVP": "IVP_text_out",
        }.get(prefix)
        if not option_key:
            return None

        texts = options.get(option_key)
        if not isinstance(texts, list) or not texts:
            return None

        template = texts[0]
        if not isinstance(template, str):
            return None

        default_complements = {
            "ICV": "resultados coerentes com as habilidades verbais observadas",
            "IOP": "resultados alinhados ao desempenho em tarefas visuoespaciais",
            "IMO": "desempenho compatível com a capacidade de atenção e memória operacional",
            "IVP": "resultado condizente com a velocidade de processamento apresentada",
        }

        prepared = template.replace("[CLASSIFICAÇÃO AQUI]", classification)
        if "[COMPLEMENTO AQUI]" in prepared:
            complement = default_complements.get(prefix, "resultados compatíveis com a pontuação obtida")
            prepared = prepared.replace("[COMPLEMENTO AQUI]", complement)

        prepared = prepared.replace(" ,", ",").replace(" .", ".").strip()
        prepared = " ".join(prepared.split())

        if prefix == "QIT" and prefix not in default_complements:
            prepared = f"{classification}. {prepared}" if prepared else classification

        return prepared or None

    @staticmethod
    def _store_if_empty(payload: Dict[str, Any], key: str, value: str) -> None:
        current = payload.get(key)
        if current is None or (isinstance(current, str) and current.strip() == ""):
            payload[key] = value

    @staticmethod
    def _to_number(raw: Any) -> Optional[float]:
        if raw is None:
            return None
        if isinstance(raw, (int, float)):
            return float(raw)
        if isinstance(raw, str):
            stripped = raw.strip().replace("%", "")
            if not stripped:
                return None
            stripped = stripped.replace(",", ".")
            try:
                return float(stripped)
            except ValueError:
                return None
        return None