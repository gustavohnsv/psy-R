# tests/test_main_window.py

from PySide6.QtCore import Qt
from app.views import MainWindow

def test_success_main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    assert not window.isVisible()

    window.show()
    assert window.isVisible()