import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("context menu practice")
        
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("one" , self))
        context.addAction(QAction("two" , self))
        context.addAction(QAction("three" , self))
        context.exec(e.globalPos())

    def mousePressEvent(self, event):
        print("Mouse pressed!")
        super(self, mainwindow).contextMenuEvent(event)

app = QApplication(sys.argv)

window = mainwindow()
window.show()
sys.exit(app.exec())
