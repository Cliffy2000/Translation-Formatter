import sys
import time
import pandas as pd
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont


application = QtWidgets.QApplication(sys.argv)
font = QFont()
font.setPointSize(12)
application.setFont(font)


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demo")
        self.setGeometry(-2000, 200, 1200, 720)

        self.fileSelectButton = QtWidgets.QPushButton("Select File", self)
        self.fileSelectButton.setGeometry(50, 50, 120, 50)
        self.fileSelectButton.clicked.connect(self.selectFile)


    def selectFile(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")
        if file:
            self.fileSelectButton.hide()
            if hasattr(self, "fileNameLabel"):
                self.fileNameLabel.setText("Loading file...")
            else:
                self.fileNameLabel = QtWidgets.QLabel("Loading file...", self)
                self.fileNameLabel.setGeometry(50, 50, 150, 50)
                self.fileNameLabel.show()
            QtWidgets.QApplication.processEvents()

            fileName = file.split('/')[-1]
            loadExcelFile(fileName)
            self.fileNameLabel.setText(fileName)

            self.fileSelectButton.setGeometry(250, 50, 130, 50)
            self.fileSelectButton.show()
            self.fileSelectButton.setText("Reselect File")


def loadExcelFile(f):
    sheetDict = pd.read_excel(f)
    for k in sheetDict.keys:
        print(k)
    return


if __name__ == "__main__":
    window = Application()
    window.show()

    sys.exit(application.exec())