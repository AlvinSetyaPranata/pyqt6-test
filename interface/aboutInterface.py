from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from handlers.aboutHandler import onButtonClicked

class AboutInterface(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button = QPushButton("about Button", self)
        self.button.clicked.connect(onButtonClicked)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
