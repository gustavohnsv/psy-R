from typing import Dict, Any

from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
)
from PySide6.QtCore import Signal

from .ui_template_fields import Ui_TelaCamposTemplate
from app.services.template.loader import TemplateFieldsLoader


class TemplateFieldsScreen(QWidget):
    next_clicked = Signal()
    back_clicked = Signal()

    def __init__(self, parent=None, loader: TemplateFieldsLoader | None = None):
        super().__init__(parent)
        self.ui = Ui_TelaCamposTemplate()
        self.ui.setupUi(self)

        # Optional: pass loader or use default
        self.loader = loader or TemplateFieldsLoader()
        self.field_widgets: Dict[str, QWidget] = {}

        # If provided, this will limit which sections to render (list of section ids)
        self.sections_to_show: list[str] | None = None

        self._build_dynamic_fields()

        self.ui.btn_voltar.clicked.connect(self.back_clicked.emit)
        self.ui.btn_avancar.clicked.connect(self.next_clicked.emit)

    def _build_dynamic_fields(self):
        layout = self.ui.verticalLayout_campos
        # remove spacer placeholder before adding sections
        self.field_widgets.clear()
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for section in self.loader.iter_sections():
            # If a filter is set, skip sections not in the list
            if self.sections_to_show and section.get("id") not in self.sections_to_show:
                continue
            group = QGroupBox(section.get("label", ""))
            group_layout = QFormLayout(group)

            for field in section.get("fields", []):
                input_widget = self._create_field_widget(field)
                self.field_widgets[field["name"]] = input_widget
                group_layout.addRow(field.get("label", field["name"]), input_widget)

            layout.addWidget(group)

        layout.addStretch(1)

    def _create_field_widget(self, field: Dict[str, Any]) -> QWidget:
        widget_type = field.get("widget", "text")
        if widget_type == "textarea":
            widget = QTextEdit()
            widget.setObjectName(f"textEdit_{field['name']}")
            return widget

        line_edit = QLineEdit()
        line_edit.setObjectName(f"lineEdit_{field['name']}")
        return line_edit

    def set_sections(self, section_ids: list[str] | None):
        """Restrict the screen to render only the given section ids (order preserved by loader)."""
        self.sections_to_show = section_ids
        self._build_dynamic_fields()

    def get_data(self) -> Dict[str, str]:
        data: Dict[str, str] = {}
        for name, widget in self.field_widgets.items():
            if isinstance(widget, QTextEdit):
                data[name] = widget.toPlainText()
            elif isinstance(widget, QLineEdit):
                data[name] = widget.text()
        return data

    def set_data(self, values: Dict[str, Any]):
        for name, widget in self.field_widgets.items():
            value = values.get(name, "")
            if isinstance(widget, QTextEdit):
                widget.setPlainText(value or "")
            elif isinstance(widget, QLineEdit):
                widget.setText(value or "")

