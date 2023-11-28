from PyQt6.QtWidgets import QWidget

class MainInterface(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Applikasi-ku")
        self.show()

