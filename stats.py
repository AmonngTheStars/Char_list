import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QWidget, QTabWidget, QTextEdit, QListWidget
)
from functools import partial
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

def set_roll_style(roll: int) -> str:
    if roll == 20 or roll == 1:
        return "color: red"
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
            stats_line = QLineEdit(str(DEFAULT_BONUS_VALUE))
            stats_line.setValidator(QIntValidator(0, 99))
            stats_line.setFixedWidth(30)
            stats_bonus = QLabel("0")
            btn_roll = QPushButton("Roll d20")
            btn_roll.clicked.connect(partial(self.roll_20, key))
            roll_result_clean = QLabel("-")
            roll_result_withbon = QLabel("-")

            self.attributes[key] = {
                "stats_line": stats_line,
                "stats_bonus": stats_bonus,
                "roll_result_clean": roll_result_clean,
                "roll_result_withbon": roll_result_withbon,
                "bonus": 0
            }
            stats_line.textChanged.connect(self.bonus_update)

            self.stats_layout.addWidget(stats_name, row, 0)
            self.stats_layout.addWidget(stats_line, row, 1)
            self.stats_layout.addWidget(stats_bonus, row, 2)
            self.stats_layout.addWidget(btn_roll, row, 3)
            self.stats_layout.addWidget(roll_result_clean, row, 4)
            self.stats_layout.addWidget(roll_result_withbon, row, 5)

        self.bonus_update()

    
    def bonus_update(self):
        for data in self.attributes.values():
            stats_line = data["stats_line"]
            stats_bonus = data["stats_bonus"]

            try:
                value = int(stats_line.text())
                bonus = bonus_check(value)
                data["bonus"] = bonus 
                stats_bonus.setText(f"Bonus: {bonus:+}")
                stats_bonus.setStyleSheet(set_bonus_style(bonus))
            except ValueError:
                stats_line.setText(DEFAULT_BONUS_VALUE)

    def roll_20(self, key):
        bonus = self.attributes[key]["bonus"]

        roll_result = random.randint(1, 20)
        label = self.attributes[key]["roll_result_clean"]
        label.setText(str(roll_result))

        label.setStyleSheet(set_roll_style(roll_result))
        
        label = self.attributes[key]["roll_result_withbon"]
        result = roll_result + bonus
        if result <= 0:
            result = 1
            label.setStyleSheet("color: orange")
        else:
            label.setStyleSheet("color: black")
        
        label.setText(str(result))
        


