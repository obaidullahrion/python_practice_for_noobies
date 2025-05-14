import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton
)

from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dummy app")
        self.setMinimumWidth(900)
        self.setMinimumHeight(600)
        self.setWindowIcon(QIcon("icon.png"))
        btn = QPushButton("click me", self)
        btn.move( 500, 500)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())