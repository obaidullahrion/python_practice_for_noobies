from sys import exit, argv
from PySide6.QtGui import QIcon , QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QApplication,   
    QToolTip,

)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mousetest")
        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.label = QLabel("Click here")
        self.label.setStyleSheet('QLabel {background-color: #A3C1DA; color: red; font-size: 30px; font-family:Ink Free}')
        self.setCentralWidget(self.label)
        self.label.setToolTip("click me")

    def mousePressEvent(self , e) :
            if e.button() == 1:
                self.label.setText("mouse left clicked")
            elif e.button() == 2:
                self.label.setText("riight button presesd")
            else:
                self.label.setText("mid-mouse button pressed")
    def mouseReleaseEvent(self, e):
        self.label.setText("released")

app = QApplication(argv)
window = mainwindow()
window.show()

exit(app.exec())