"""
This is a file that will be used to create a main window for the application.
This is only a UI.
Detailed functions and methods will be implemented in the ../modules/*.py file.
"""

import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        file = QFile("FitYou_App/App/configs/ui/MainUI.ui")
        if file.open(QIODevice.ReadOnly):
            loader = QUiLoader()
            self.ui = loader.load(file, self)
            file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit((app.exec()))
    except:
        print("exiting")