import sys
import PySide6
from PySide6.QtCore import Qt , QSize
from PySide6.QtGui import QIcon , QPixmap, QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QApplication,
    QToolTip
    
)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("basic window")
        button = QPushButton("click me" , self)
        self.setCentralWidget(button)
        self.setMinimumHeight(300)
        self.setMinimumWidth(500)
        icon=QIcon("icon.png")
        self.setWindowIcon(icon)
        QToolTip.setFont(QFont("Ink Free",10, QFont.Bold))
        self.setToolTip("this is the mainwindow")
        button.setToolTip("button tooltip")
        self.logo()


    def logo(self):

        logoalttxt = QLabel("kittycat" , self)
        logo = QIcon("icon.png")
        logopixmap = logo.pixmap(50 , 50 ,QIcon.Active , QIcon.On)
        logoalttxt.setPixmap(logopixmap)
        logoalttxt.setToolTip("kittylogo")

app = QApplication(sys.argv)

window = mainwindow()
window.show()

app.exec()