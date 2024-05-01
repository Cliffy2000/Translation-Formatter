import sys
import pandas as pd
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demo")
        self.setGeometry(-2000, 200, 1200, 720)

        self.fileSelectButton = QtWidgets.QPushButton("Select File", self)
        self.fileSelectButton.setGeometry(50, 50, 120, 50)
        self.fileSelectButton.clicked.connect(self.selectFile)


    def selectFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")
        if fileName:
            self.fileSelectButton.setGeometry(250, 50, 130, 50)
            self.fileSelectButton.setText("Reselect File")

            self.fileNameLabel = QtWidgets.QLabel(fileName.split('/')[-1], self)
            self.fileNameLabel.setGeometry(50, 50, 150, 50)
            self.fileNameLabel.show()


application = QtWidgets.QApplication(sys.argv)
font = QFont()
font.setPointSize(12)
application.setFont(font)

window = Application()
window.show()

sys.exit(application.exec())