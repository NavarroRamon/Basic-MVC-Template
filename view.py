from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QLineEdit, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class View(QWidget):
    style = """
        QWidget {
            background-color: #333;
            color: #eee;
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        QLineEdit {
            background-color: #444;
            color: #eee;
            border: none;
            padding: 5px;
        }
        QPushButton {
            background-color: #555;
            color: #eee;
            border: none;
            padding: 5px;
        }
        QListWidget {
            background-color: #444;
            color: #eee;
            border: none;
            padding: 5px;
        }
    """

    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 5, 10, 10)
        self.setStyleSheet(self.style)

        self.setWindowTitle('Basic MVC Template')

        # Create label and set font and alignment
        self.title_label = QLabel('Basic MVC Template', self)
        self.title_label.setAlignment(Qt.AlignCenter)
        font = self.title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)

        self.items_list = QListWidget()
        self.add_button = QPushButton("Add")
        self.remove_button = QPushButton("Remove")
        self.item_text = QLineEdit()
        self.item_text.setPlaceholderText("Enter new item here...")


        # Add list widget and button layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.title_label, 0, 0, 1, 2)
        # Add list widget and button layout
        layout.addWidget(self.items_list, 1, 0, 2, 2)
        layout.addWidget(self.add_button, 3, 0)
        layout.addWidget(self.remove_button, 3, 1)

        # Add item text input
        layout.addWidget(self.item_text, 4, 0, 1, 2)
        # Set all rows to have the same height
        layout.setRowStretch(0, 0.7)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
