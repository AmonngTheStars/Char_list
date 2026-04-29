import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QWidget, QTabWidget, QTextEdit, QListWidget
)
DEFAULT_BONUS_VALUE = 10
DEFAULT_FONT_SIZE = 20
STATS = [
    ("str", "Strange"),
    ("dex", "Dexterity"),
    ("int", "Intellegence"),
    ("con", "Constitution"),
    ("wis", "Wisdom"),
    ("cha", "Charisma"),
]

def bonus_check(value: int) -> int:
    return (value-10) // 2

def set_bonus_style(bonus: int) -> str:
    if bonus < 0:
        return "color: red"
    elif bonus > 0:
        return "color:green"
    return "color: black"
    
class Stats(QWidget):
    def __init__(self):
        super().__init__()

        self.stats_layout = QGridLayout(self)
        self.stats_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.stats_layout.setColumnStretch(10, 1)
        self.stats_layout.setRowStretch(10, 1)
        self.stats_layout.setHorizontalSpacing(15)
        self.stats_layout.setVerticalSpacing(8)

        self.attributes = {}
        for row, (key, title) in enumerate(STATS):
            stats_name = QLabel(title)
            #stats_name.setFixedWidth(80)
            stats_line = QLineEdit(str(DEFAULT_BONUS_VALUE))
            stats_line.setValidator(QIntValidator(0, 99))
            stats_line.setFixedWidth(30)
            stats_bonus = QLabel("0")

            self.attributes[key] = {
                "stats_line": stats_line,
                "stats_bonus" : stats_bonus
            }

            stats_line.textChanged.connect(self.bonus_update)

            self.stats_layout.addWidget(stats_name, row, 0)
            self.stats_layout.addWidget(stats_line, row, 1)
            self.stats_layout.addWidget(stats_bonus, row, 2)
            #self.stats_layout.addWidget(QWidget(), 0, 3)
            #self.stats_layout.setColumnStretch(3, 1)

        self.bonus_update()

    def bonus_update(self):
        for data in self.attributes.values():
            stats_line = data["stats_line"]
            stats_bonus = data["stats_bonus"]

            try:
                value = int(stats_line.text())
                bonus = bonus_check(value)
                stats_bonus.setText(f"Bonus: {bonus:+}")
                stats_bonus.setStyleSheet(set_bonus_style(bonus))
            except ValueError:
                stats_line.setText(DEFAULT_BONUS_VALUE)
            

