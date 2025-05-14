from msilib.schema import Icon
from sys import argv, exit
from PySide6.QtGui import QIcon , QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QPushButton

)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dreaxfly")
        Icon = QIcon("practice_icon.png")
        self.setWindowIcon(Icon)
        self.setMinimumWidth(900)
        self.setMinimumHeight(500)
        self.home()
        self.title()
        self.bannerimage()
        self.text()
    def home(self):
        homebutton = QPushButton("🏠", self)
        homebutton.setGeometry(0 ,0 , 50 , 50)
        

    def title(self):
        homebutton = QPushButton(self)
        homebutton.setGeometry(50 ,0 , 850 , 50)
        button=QPushButton()
        homebutton.setText("Wanna fly!")
        homebutton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red; font-size: 30px; font-family:Ink Free}')



    def text(self):
        text = QLabel(" click below:3", self)

        text.move(450 ,250)

    def bannerimage(self):
        imagealtlebel = QLabel("bannerimage", self)
        bannerimage = QIcon("catfly.jpg")
        bannerpixed = bannerimage.pixmap(500 , 50, QIcon.Active , QIcon.On)
        img = imagealtlebel.setPixmap(bannerpixed)
        imagealtlebel.move(450 ,350)

app = QApplication(argv)
window = mainwindow()

window.show()

exit(app.exec())

