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
from stats import Stats
from char_lore import Story

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle("Character list")
        self.tabs = QTabWidget()
        self.tabs.addTab(Stats(), "Attributes")
        self.tabs.addTab(Story(), "Character`s lore")

        self.setCentralWidget(self.tabs)

app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget {
        font-size: 16px;
    }

    QTextEdit {
        font-size: 16px;
    }

    QLabel {
        font-size: 18px;
    }
""")
window = MainWindow()
window.show()
sys.exit(app.exec())