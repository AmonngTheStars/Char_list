import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QWidget, QTabWidget, QTextEdit, QListWidget
)

class Story(QWidget):
    def __init__(self):
        super().__init__()

        story_layout = QGridLayout(self)

        char_story_label = QLabel("Character`s story")
        char_story = QTextEdit()
        char_story.setPlaceholderText("Arthas was born...")

        char_character_label = QLabel("Character`s character")
        char_character = QTextEdit()
        char_character.setPlaceholderText("He is brave and proud...")

        story_layout.addWidget(char_story_label)
        story_layout.addWidget(char_story)
        story_layout.addWidget(char_character_label)
        story_layout.addWidget(char_character)