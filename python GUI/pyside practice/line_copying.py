import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("text copying")
        self.setMinimumWidth(900)
        self.setMinimumHeight(600)
        self.setWindowIcon(QIcon("icon.png"))

        
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        btn = QPushButton("click me", self)
        btn.move( 500, 500)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())