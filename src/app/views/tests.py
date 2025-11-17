from functools import partial
from PySide6.QtWidgets import QWidget, QPushButton, QStackedWidget, QSpinBox
from PySide6.QtCore import Signal

from .ui_tests import Ui_TelaTestes
from app.services.test_tables_loader import TestTablesLoader


class TestsScreen(QWidget):
    avancar_clicado = Signal()
    voltar_clicado = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TelaTestes()
        self.ui.setupUi(self)

        self.ui.btn_avancar.clicked.connect(self.avancar_clicado.emit)
        self.ui.btn_voltar.clicked.connect(self.voltar_clicado.emit)

        self.configurar_botoes_teste()

        # Load test configuration tables
        try:
            self.tables_loader = TestTablesLoader()
            self.test_tables = self.tables_loader.load_all()
        except Exception:
            self.test_tables = {}

        # Apply loaded tables into UI (titles, ranges)
        self._apply_tables_to_ui()

    def configurar_botoes_teste(self):
        stacked_forms = self.ui.stackedWidget_formularios

        botoes_testes = [
            self.ui.btn_wisc4, self.ui.btn_ravlt, self.ui.btn_bpa2,
            self.ui.btn_neupsilin, self.ui.btn_srs2, self.ui.btn_etdah,
            self.ui.btn_cars2, self.ui.btn_htp, self.ui.btn_fdt,
        ]

        for i, btn in enumerate(botoes_testes):
            # O índice 0 é a página "Selecione...", então o botão 1 (i=0) vai para a página 1
            btn.clicked.connect(partial(self.mostrar_form_teste, stacked_forms, i + 1))

    def mostrar_form_teste(self, stacked_widget, index):
        if index < stacked_widget.count():
            stacked_widget.setCurrentIndex(index)
        else:
            print(f"Aviso: Formulário de teste (índice {index}) não encontrado.")

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
        Returns a dict keyed by test prefix (e.g. 'wisc4') containing widget values.
        """
        results = {}

        # mapping of test key -> (incluir_checkbox_attr, page_widget_prefix)
        mapping = {
            "wisc": ("checkBox_incluir_wisc4", "wisc4"),
            "ravlt": ("checkBox_incluir_ravlt", "ravlt"),
            "bpa": ("checkBox_incluir_bpa2", "bpa2"),
            "neupsilin": ("checkBox_incluir_neupsilin", "neupsilin"),
            "srs": ("checkBox_incluir_srs2", "srs2"),
            "etdah": ("checkBox_incluir_etdah", "etdah"),
            "cars": ("checkBox_incluir_cars2", "cars2"),
            "htp": ("checkBox_incluir_htp", "htp"),
            "fdt": ("checkBox_incluir_fdt", "fdt"),
        }

        for key, (checkbox_attr, prefix) in mapping.items():
            incluir = getattr(self.ui, checkbox_attr, None)
            if incluir is None:
                continue
            if not incluir.isChecked():
                # skip tests not included
                continue

            # collect all spinboxes on the page identified by prefix
            page_values = {}
            for name in dir(self.ui):
                if name.startswith("spin") and prefix in name:
                    widget = getattr(self.ui, name)
                    if isinstance(widget, QSpinBox):
                        page_values[name] = widget.value()

            # fallback: collect any spinboxes in the page group box
            if not page_values:
                # try to find groupBox with prefix and collect spinboxes underneath
                for attr in dir(self.ui):
                    if prefix in attr and "groupBox" in attr:
                        gb = getattr(self.ui, attr)
                        # iterate children
                        for child in gb.findChildren(QSpinBox):
                            page_values[child.objectName()] = child.value()

            results[prefix] = page_values

        return results