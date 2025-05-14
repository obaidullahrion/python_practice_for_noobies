import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel
)

from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dummy app")
        self.setMinimumWidth(900)
        self.setMinimumHeight(600)
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
        self.logo()


    def logo(self):
        logo = QIcon("icon.png")
        label1 = QLabel("sample", self)
        setlogo = logo.pixmap(50,50 , QIcon.Active , QIcon.On)
        label1.setPixmap(setlogo)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
sys.exit()