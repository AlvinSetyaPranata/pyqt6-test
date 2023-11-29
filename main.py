import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton

from interface.homeInterface import HomeInterface
from interface.aboutInterface import AboutInterface


class MainInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget(self)

        self.home_page = HomeInterface()
        self.about_page = AboutInterface()

        self.home_btn = QPushButton("To home", self)
        self.about_btn = QPushButton("To About", self)

        self.home_btn.clicked.connect(self.to_page_1)
        self.about_btn.clicked.connect(self.to_page_2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.home_btn)
        layout.addWidget(self.about_btn)
        
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.about_page)

    def to_page_1(self):
        self.stack.setCurrentIndex(0)

    def to_page_2(self):
        self.stack.setCurrentIndex(1)





app = QApplication(sys.argv)
window = MainInterface()
window.show()
sys.exit(app.exec())