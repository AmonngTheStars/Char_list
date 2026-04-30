import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QIntValidator, QFont
)
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QWidget, QTabWidget, QTextEdit, QListWidget
)
from main_window import MainWindow
from pathlib import Path

app = QApplication(sys.argv)
style_path = Path(__file__).parent / "styles.qss"

with open(style_path, "r", encoding="utf-8") as f:
    style = f.read()
app.setStyleSheet(style)
window = MainWindow()
window.show()
sys.exit(app.exec())