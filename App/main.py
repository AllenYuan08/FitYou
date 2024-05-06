import sys
from PySide6.QtWidgets import QApplication
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.login_window import MainApplication

def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()