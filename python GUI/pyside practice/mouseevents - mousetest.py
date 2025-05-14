from sys import exit, argv
from PySide6.QtGui import QIcon , QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QApplication,
    QToolTip

)

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mousetest- click counter")
        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.label = QLabel("Click here")
        self.label.setStyleSheet('QLabel {color: red; font-size: 50px; font-family:Ink Free; margin-left: 50px}')
        self.setCentralWidget(self.label)
        self.label.setToolTip("click me")
        
    global a 
    a = []

    def mousePressEvent(self , e) :
        # self.label.setText("pressed")
        a.append(1)
        
    def mouseReleaseEvent(self, e):
        m = a.count(1)
        self.label.setText(str(m))
        # print(a.count(1))
    # def mouseMoveEvent(self, e):
    #     self.label.setText("moving")


app = QApplication(argv)
window = mainwindow()
window.show()

exit(app.exec())