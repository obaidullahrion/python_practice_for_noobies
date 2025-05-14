from ast import arg
from sys import argv, exit
from PySide6.QtGui import  QIcon, QFont
# from PySide6.QtCore import 
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QMessageBox
)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("signals and slots")
        self.setMinimumHeight(500)
        self.setMinimumWidth(850)
        self.exit_button()
        self.about_button()


    def exit_button(self):
        self.button = QPushButton("exit" , self)
        self.button.setGeometry (50 , 50 , 50 ,50 )
        self.button.clicked.connect(self.warning)

    def about_button(self):
        self.about_button= QPushButton("about" , self)
        self.about_button.setGeometry (100 , 100 , 50 ,50 )
        self.about_button.clicked.connect(self.about)
        self.about_button.setCheckable(True)


    def about(self , checked):
        aboutbox = QMessageBox.about(self.about_button , "about" , "Thank you for using our application" )

    def warning(self):
        box = QMessageBox.question(self, "confirmation" ,   "are you sure to close ? " , QMessageBox.Yes | QMessageBox.No)

        if box == QMessageBox.Yes:
            exit()
        else:
            pass

    def close(self):
        exit()



app = QApplication(argv)
window = mainwindow()
window.show()

exit(app.exec())