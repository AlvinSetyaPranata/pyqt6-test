import sys
from PyQt6.QtWidgets import QApplication

from interface.mainInterface import MainInterface



app = QApplication(sys.argv)
window = MainInterface()
sys.exit(app.exec())