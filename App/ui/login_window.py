import sys
from PySide6 import QtGui, QtWidgets, QtCore

from ui.Sign_Up import Ui_Dialog as Signup
from ui.welcome_window import Ui_Dialog
import App.modules.fitness as fitness
import App.modules.diet as diet
import App.modules.login as login
from ui.main_window import MainApplication as MainUI

class MainApplication(QtWidgets.QMainWindow):
    show_signup_signal = QtCore.Signal()  # 自定义信号

    def __init__(self):
        super(MainApplication, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_connections()
        self.main_application = None
        
        self.signup_window = SignUP()
        self.signup_window.show_login_signal.connect(self.show)  # 连接信号
        self.show_signup_signal.connect(self.signup_window.show)  # 连接信号

    def setup_connections(self):
        self.ui.Signup.clicked.connect(self.show_signup_signal.emit)  # 发射信号
        self.ui.Login.clicked.connect(self.login)
        
    def login(self):
        username = str(self.ui.username.text())
        password = str(self.ui.password.text())
        
        if login.validate_login(username, password):
            QtWidgets.QMessageBox.information(self, "Success", "You have successfully logged in!")
            self.open_main_application(username)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password. Please try again.")
    
    def open_main_application(self, username):
        if not self.main_application:
            self.main_application = MainUI(username)  # 创建MainApplication实例
        self.hide()  # 隐藏登录窗口
        self.main_application.show()  # 显示主窗口
    

        
class SignUP(QtWidgets.QMainWindow):
    show_login_signal = QtCore.Signal()  # 自定义信号

    def __init__(self):
        super(SignUP, self).__init__()
        self.ui = Signup()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.Signup.clicked.connect(self.signup)
        self.ui.Signup_2.clicked.connect(self.go_back)
        
    def signup(self):
        name = self.ui.name.text()
        phnum = self.ui.phnum.text()
        username = self.ui.username.text()
        password = self.ui.password.text()
        confirm_password = self.ui.confirmPassword.text()
        if password == confirm_password:
            login.sign_up(name, phnum, username, password, confirm_password)
            QtWidgets.QMessageBox.information(self, 'Success', 'Registration successful!')
            self.create_user_database(username)
            self.show_login_signal.emit()  # 发射信号返回登录窗口
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Passwords do not match. Please try again.')
            
    def go_back(self):
        self.hide()
        self.show_login_signal.emit()  # 发射信号
        
    def create_user_database(self, username):
        excel_file_path1 = "./Data/Database_files/Fitness_Records.xlsx"
        login.create_databases_for_user(username, excel_file_path1, sheet_name="Fitness_Records")
        excel_file_path2 = "./Data/Database_files/Diet_Records.xlsx"
        login.create_databases_for_user(username, excel_file_path2, sheet_name="Diet_Records")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec())
