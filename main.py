from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 500, 500)
    win.setWindowTitle("ReRa Application")

    label = QtWidgets.QLabel(win)
    label.setText("Test Label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()