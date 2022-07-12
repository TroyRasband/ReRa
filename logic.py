from blank2 import *

import sys

class AppGui(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickMe)
        #self.pushButton.clicked.connect(self.showName)

    def clickMe(self):
        print("I have been clicked!")


app = QtWidgets.QApplication(sys.argv) #"Not actually needed"
MainWindow = QtWidgets.QMainWindow()

ui = AppGui(MainWindow)

MainWindow.show()
app.exec_()
