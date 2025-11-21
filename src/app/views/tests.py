from functools import partial
from typing import Dict, Any

from PySide6.QtWidgets import QWidget, QPushButton, QStackedWidget, QSpinBox
from PySide6.QtCore import Signal

from .ui_tests import Ui_TelaTestes
from app.services.test_tables_loader import TestTablesLoader


# Mapping from UI widget names to canonical template field names expected
# downstream (e.g., by LaudoDataModel/TestResultClassifier).
TEST_FIELD_CONFIG: Dict[str, Dict[str, Any]] = {
    "wisc": {
        "checkbox": "checkBox_incluir_wisc4",
        "fields": {
            "spinBox_icv_wisc4": "ICV_WISC",
            "spinBox_iop_wisc4": "IOP_WISC",
            "spinBo_imo_wisc4": "IMO_WISC",
            "spinBox_ivp_wisc4": "IVP_WISC",
            "spinBox": "DIGS_WISC",
            "spinBox_2": "SNL_WISC",
            "spinBox_3": "ARIT_WISC",
            "spinBox_4": "SEME_WISC",
            "spinBox_5": "RV_WISC",
            "spinBox_6": "RNV_WISC",
            "spinBox_7": "CUBE_WISC",
            "spinBox_8": "VP_WISC",
        },
    },
    "ravlt": {
        "checkbox": "checkBox_incluir_ravlt",
        "fields": {
            "spinBox_r1_ravlt": "ALT_RAVLT",
            "spinBox_r2_ravlt": "VE_RAVLT",
            "spinBox_r3_ravlt": "IP_RAVLT",
            "spinBox_r4_ravlt": "IR_RAVLT",
        },
    },
    "bpa": {
        "checkbox": "checkBox_incluir_bpa2",
        "fields": {
            "spinBox_ac_bpa2": "AC_BPA",
            "spinBox_ad_bpa2": "AD_BPA",
            "spinBox_aa_bpa2": "AA_BPA",
        },
    },
    "neupsilin": {
        "checkbox": "checkBox_incluir_neupsilin",
        "fields": {
            "spinBox_tarefas_neupsilin": "TASK_NEUP",
        },
    },
    "srs": {
        "checkbox": "checkBox_incluir_srs2",
        "fields": {
            "spinBox_TODO_srs2": "SRS_ESCORE_TOTAL",
        },
    },
    "etdah": {
        "checkbox": "checkBox_incluir_etdah",
        "fields": {
            "spinBox_fac1_etdah": "F1_ETDAH",
            "spinBox_fac2_etdah": "F2_ETDAH",
            "spinBox_fac3_etdah": "F3_ETDAH",
            "spinBox_fac4_etdah": "F4_ETDAH",
        },
    },
    "cars": {
        "checkbox": "checkBox_incluir_cars2",
        "fields": {
            "spinBox_TODO_cars2": "CARS_PONTUACAO",
        },
    },
    "fdt": {
        "checkbox": "checkBox_incluir_fdt",
        "fields": {
            "spinBox_flexcog_fdt": "FC_FDT",
            "spinBox_ctlinib_fdt": "CI_FDT",
        },
    },
}


class TestsScreen(QWidget):
    next_clicked = Signal()
    back_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaTestes()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.next_clicked.emit)
        self.ui.btn_voltar.clicked.connect(self.back_clicked.emit)

        self.setup_test_buttons()

        # Load test configuration tables
        try:
            self.tables_loader = TestTablesLoader()
            self.test_tables = self.tables_loader.load_all()
        except Exception:
            self.test_tables = {}

        # Apply loaded tables into UI (titles, ranges)
        self._apply_tables_to_ui()

    def setup_test_buttons(self):
        stacked_forms = self.ui.stackedWidget_formularios

        test_buttons = [
            self.ui.btn_wisc4, self.ui.btn_ravlt, self.ui.btn_bpa2,
            self.ui.btn_neupsilin, self.ui.btn_srs2, self.ui.btn_etdah,
            self.ui.btn_cars2, self.ui.btn_htp, self.ui.btn_fdt,
        ]

        for i, btn in enumerate(test_buttons):
            # Index 0 is the "Select..." page, so button 1 (i=0) goes to page 1
            btn.clicked.connect(partial(self.show_test_form, stacked_forms, i + 1))

    def show_test_form(self, stacked_widget, index):
        if index < stacked_widget.count():
            stacked_widget.setCurrentIndex(index)
        else:
            print(f"Warning: Test form (index {index}) not found.")

    def _apply_tables_to_ui(self):
        """Apply loaded test tables into UI labels and widgets.

        Actions:
        - set test page title labels from table 'teste'
        - set reasonable ranges on spinboxes
        """
        if not getattr(self, "test_tables", None):
            return

        # set max/min defaults for all spinboxes to accept common score ranges
        for attr in dir(self.ui):
            try:
                widget = getattr(self.ui, attr)
            except Exception:
                continue
            if isinstance(widget, QSpinBox):
                widget.setRange(0, 200)

        # map possible table keys to UI prefixes
        table_to_prefix = {
            "wisc": "wisc4",
            "ravlt": "ravlt",
            "bpa": "bpa2",
            "neupsilin": "neupsilin",
            "srs": "srs2",
            "etdah": "etdah",
            "cars": "cars2",
            "htp": "htp",
            "fdt": "fdt",
        }

        for table_key, data in self.test_tables.items():
            prefix = table_to_prefix.get(table_key)
            if not prefix:
                continue
            label_attr = f"label_titulo_{prefix}"
            label = getattr(self.ui, label_attr, None)
            if label and isinstance(data, dict):
                title = data.get("teste") or data.get("name")
                if title:
                    label.setText(title)

    def get_data(self):
        """Collect test results from the UI.

        Only includes tests with the 'incluir' checkbox checked.
        Returns a flat dict where keys are canonical template field names.
        """
        results: Dict[str, Any] = {}

        for config in TEST_FIELD_CONFIG.values():
            checkbox_name = config.get("checkbox")
            if not checkbox_name:
                continue
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox is None or not checkbox.isChecked():
                continue

            for widget_name, field_name in config.get("fields", {}).items():
                widget = getattr(self.ui, widget_name, None)
                if isinstance(widget, QSpinBox):
                    results[field_name] = widget.value()

        return results