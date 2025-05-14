import sys
from PySide6 import QtWidgets, QtGui

def ask_question():
    result = QtWidgets.QMessageBox.question(None, "Question", "oil amman's ass?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    if result == QtWidgets.QMessageBox.Yes:
        QtWidgets.QMessageBox.information(None, "Information", "contact arab for oil")

    elif result == QtWidgets.QMessageBox.No:
        QtWidgets.QMessageBox.information(None, "Information", " gae test : passed ")



def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Example")

    button = QtWidgets.QPushButton("Ask Question", parent=window)
    button.clicked.connect(ask_question)

    layout = QtWidgets.QVBoxLayout(window)
    layout.addWidget(button)

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()