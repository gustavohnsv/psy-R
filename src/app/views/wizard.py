from PySide6.QtWidgets import (
    QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QListWidget, QLineEdit, QTextEdit, QGridLayout
)
from PySide6.QtCore import Qt, QSize

from app.core.models import ReportModel
from app.core.report import fill_report_model, export_to_json, export_to_docx, export_to_txt


class WizardMainWindow(QMainWindow):
    """Clean single-definition Wizard window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Psy-R - Wizard")
        # Apply a simple dark theme + typography similar to the Figma screens
        self.setStyleSheet("""
        QWidget { background: #333333; color: #FFFFFF; }
        QLabel#heading { font-size: 36px; font-weight: 800; color: #FFFFFF; }
        QLineEdit, QTextEdit { background: #FFFFFF; color: #000000; border: 2px solid #333333; padding: 8px; border-radius:6px; }
        QPushButton#primary { background: #7A00FF; color: #FFFFFF; border-radius: 8px; padding: 10px 20px; font-weight: 700; }
        QPushButton#navcircle { background: transparent; border: 4px solid #777777; color: #777777; border-radius: 28px; min-width:56px; min-height:56px; font-size:20px; }
        QPushButton#ghost { background: rgba(255,255,255,0.06); color: #FFFFFF; border-radius: 28px; padding: 12px 28px; }
        QTextEdit { min-height: 140px; }
        """)

        self.model = ReportModel()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # pages
        self.stack.addWidget(self._page_upload())
        self.stack.addWidget(self._page_patient())
        self.stack.addWidget(self._page_tests())
        self.stack.addWidget(self._page_conclusion())

        # corner navigation buttons
        self._add_nav_bar()

    def _page_upload(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel("Upload do template de laudo (JSON / DOCX / ODT)")
        label.setObjectName('heading')
        layout.addWidget(label)
        btn = QPushButton("Selecionar template...")
        btn.setObjectName('primary')
        btn.clicked.connect(self._select_template)
        layout.addWidget(btn)
        self.template_label = QLabel("Nenhum template carregado")
        layout.addWidget(self.template_label)
        return page

    def _page_patient(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        h = QLabel("Dados do paciente")
        h.setObjectName('heading')
        layout.addWidget(h)
        self.patient_name = QLineEdit()
        self.patient_name.setPlaceholderText("Nome")
        self.patient_age = QLineEdit()
        self.patient_age.setPlaceholderText("Idade")
        self.patient_birth = QLineEdit()
        # máscara para data: DD/MM/AAAA
        self.patient_birth.setInputMask("00/00/0000")
        self.patient_birth.setPlaceholderText("DD/MM/AAAA")
        layout.addWidget(self.patient_name)
        layout.addWidget(self.patient_age)
        layout.addWidget(self.patient_birth)
        return page

    def _page_tests(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        h = QLabel("Selecione testes e preencha valores")
        h.setObjectName('heading')
        layout.addWidget(h)

        grid = QGridLayout()
        self.test_buttons = []
        tests = ["WISC", "WAIS", "Raven", "Bender", "TDE", "BGT", "TMT", "Stroop"]
        for i, t in enumerate(tests):
            b = QPushButton(t)
            b.setObjectName('ghost')
            b.setCheckable(True)
            b.clicked.connect(lambda checked, name=t: self._on_test_toggled(name, checked))
            grid.addWidget(b, i // 4, i % 4)
            self.test_buttons.append(b)

        layout.addLayout(grid)

        # JSON-like editor for raw values
        self.raw_values = QTextEdit()
        self.raw_values.setPlaceholderText('{"WISC": {"subtest": 10}}')
        layout.addWidget(self.raw_values)

        add_btn = QPushButton("Adicionar teste ao relatório")
        add_btn.setObjectName('primary')
        add_btn.clicked.connect(self._add_test_from_ui)
        layout.addWidget(add_btn)

        self.tests_list = QListWidget()
        layout.addWidget(self.tests_list)

        return page

    def _page_conclusion(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        h = QLabel("Conclusão e revisão")
        h.setObjectName('heading')
        layout.addWidget(h)

        self.summary = QTextEdit()
        layout.addWidget(self.summary)
        export_btn = QPushButton("Gerar arquivo (JSON)")
        export_btn.setObjectName('primary')
        export_btn.clicked.connect(self._export_report_json)
        layout.addWidget(export_btn)
        export_btn2 = QPushButton("Gerar arquivo (DOCX)")
        export_btn2.setObjectName('primary')
        export_btn2.clicked.connect(self._export_report_docx)
        layout.addWidget(export_btn2)
        export_btn3 = QPushButton("Gerar arquivo (TXT)")
        export_btn3.setObjectName('primary')
        export_btn3.clicked.connect(self._export_report_txt)
        layout.addWidget(export_btn3)
        return page

    def _add_nav_bar(self):
        # corner circular nav buttons (gray)
        self.nav_prev_circle = QPushButton("←", self)
        self.nav_prev_circle.setObjectName('navcircle')
        self.nav_prev_circle.clicked.connect(self._prev_page)
        self.nav_prev_circle.setFixedSize(QSize(56, 56))

        self.nav_next_circle = QPushButton("→", self)
        self.nav_next_circle.setObjectName('navcircle')
        self.nav_next_circle.clicked.connect(self._next_page)
        self.nav_next_circle.setFixedSize(QSize(56, 56))

        # initial placement will be handled in resizeEvent

    def resizeEvent(self, event):
        super().resizeEvent(event)
        margin = 16
        w = self.width()
        h = self.height()
        self.nav_prev_circle.move(margin, h - self.nav_prev_circle.height() - margin)
        self.nav_next_circle.move(w - self.nav_next_circle.width() - margin, h - self.nav_next_circle.height() - margin)

    def _select_template(self):
        path, _ = QFileDialog.getOpenFileName(self, "Selecionar template", "", "Templates (*.json *.docx *.odt)")
        if not path:
            return
        self.model.metadata['template_path'] = path
        self.template_label.setText(path)

    def _on_test_toggled(self, name, checked):
        # visual toggle only; actual addition happens with "Adicionar teste ao relatório"
        for b in self.test_buttons:
            if b.text() == name:
                b.setChecked(checked)

    def _add_test_from_ui(self):
        try:
            import json
            values = json.loads(self.raw_values.toPlainText() or "{}")
        except Exception:
            values = {}
        # add all checked tests
        for b in self.test_buttons:
            if b.isChecked():
                tid = b.text()
                self.model.add_test(tid, values.get(tid, {}))
                self.tests_list.addItem(f"{tid}: {values.get(tid, {})}")

    def _prev_page(self):
        idx = self.stack.currentIndex()
        if idx > 0:
            self.stack.setCurrentIndex(idx - 1)

    def _next_page(self):
        idx = self.stack.currentIndex()
        if idx < self.stack.count() - 1:
            # when moving to conclusion, fill conversions
            if idx + 1 == self.stack.count() - 1:
                try:
                    fill_report_model(self.model)
                    summary_text = f"Paciente: {self.patient_name.text()}\nIdade: {self.patient_age.text()}\nNascimento: {self.patient_birth.text()}\n\nTestes:\n"
                    for t in self.model.tests:
                        summary_text += f"- {t.test_id}: {t.converted_values}\n"
                    self.summary.setPlainText(summary_text)
                except Exception:
                    pass
            self.stack.setCurrentIndex(idx + 1)

    def _export_report_json(self):
        path, _ = QFileDialog.getSaveFileName(self, "Salvar relatório", "", "JSON (*.json)")
        if not path:
            return
        try:
            export_to_json(self.model, path)
        except Exception as e:
            print('Erro export JSON', e)

    def _export_report_docx(self):
        path, _ = QFileDialog.getSaveFileName(self, "Salvar relatório", "", "Word (*.docx)")
        if not path:
            return
        try:
            export_to_docx(self.model, path)
        except Exception as e:
            print('Erro export DOCX', e)

    def _export_report_txt(self):
        path, _ = QFileDialog.getSaveFileName(self, "Salvar relatório", "", "Text (*.txt)")
        if not path:
            return
        try:
            export_to_txt(self.model, path)
        except Exception:
            # fallback para JSON se der problema
            export_to_json(self.model, path + ".json")
