import sys, os
import random
import pandas as pd
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import QTimer, QRect, Qt
from PySide6.QtGui import QPixmap, QStandardItem, QStandardItemModel

from ui.MainUI import Ui_MainWindow
import App.modules.fitness as fitness
import App.modules.diet as diet
import App.modules.profile as profile

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self, username=None):
        super(MainApplication, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = username
        self.setup_connections()
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 设置时间间隔为1000毫秒（1秒）
        self.timer.timeout.connect(self.update_lcd)
        # 记录时间
        self.time = 0
        
        # Diet
        self.model = QStandardItemModel(self.ui.listView)
        self.ui.listView.setModel(self.model)
        
        # Profile
        self.ui.tabWidget_2.currentChanged.connect(self.tab_selected)

    def setup_connections(self):
        # 连接界面的按钮到相应的槽函数
        # Fitness
        self.ui.pushButton_10.clicked.connect(self.search_fitness)
        self.ui.pushButton_7.clicked.connect(self.start_timer)
        self.ui.pushButton_8.clicked.connect(self.pause_timer)
        self.ui.pushButton_9.clicked.connect(self.reset_timer)
        
        # Diet
        self.ui.pushButton_12.clicked.connect(self.search_diet)
        self.ui.pushButton_11.clicked.connect(self.upload_food_image)
        
        # Profile
        self.ui.pushButton_4.clicked.connect(self.save_user_info)
        self.ui.pushButton_5.clicked.connect(self.save_fitness_records)
        self.ui.pushButton_6.clicked.connect(self.save_diet_records)
        
        
    def search_fitness(self):
        search_fitness_name = self.ui.lineEdit_16.text()
        fitness.search_fitness(search_fitness_name, self.ui.textEdit, self.ui.label_10)
        # print(message)
        # return message
        
    def update_lcd(self):
        self.time += 1
        self.ui.lcdNumber.display(self.time)
    
    def start_timer(self):
        self.timer.start()  # 开始定时器

    def pause_timer(self):
        self.timer.stop()  # 停止定时器

    def reset_timer(self):
        self.timer.stop()  # 停止定时器
        self.time = 0      # 重置时间
        self.ui.lcdNumber.display(0)  # 显示0
        
    def search_diet(self):
        search_diet_name = str(self.ui.comboBox_18.currentText())
        diet.search_diet(search_diet_name, self.model, self.ui.label_12)
        
    def upload_food_image(self):
        diet.upload_food_image(self, self.ui.label_11)
        
    def tab_selected(self, index):
        # 根据索引获取用户名
        self.update_list_widget(self.username)
    
    def update_list_widget(self, username):
        list_widget_username = self.ui.listWidget
        list_widget_age = self.ui.listWidget_2
        list_widget_sex = self.ui.listWidget_3
        list_widget_weight = self.ui.listWidget_4
        profile.get_user_info(username, list_widget_username, list_widget_age, list_widget_sex, list_widget_weight)
        
    def save_user_info(self):
        name = str(self.ui.lineEdit.text())
        age = int(self.ui.lineEdit_2.text())
        sex = str(self.ui.comboBox.currentText())
        weight = str(self.ui.lineEdit_3.text())
        
        if profile.save_user_info(self.username, name, age, sex, weight):
            QtWidgets.QMessageBox.information(self, 'Success', 'User data updated successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to update user data.')
            
    def save_fitness_records(self):
        time1 = str(os.times())
        sports1 = str(self.ui.comboBox_2.currentText())
        duration1 = str(self.ui.comboBox_3.currentText())
        
        if profile.save_fitness_records(self.username, time1, sports1, duration1):
            QtWidgets.QMessageBox.information(self, 'Success', 'Fitness records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save fitness records.')
            
        time2 = str(os.times())
        sports2 = str(self.ui.comboBox_4.currentText())
        duration2 = str(self.ui.comboBox_5.currentText())
        
        if profile.save_fitness_records(self.username, time2, sports2, duration2):
            QtWidgets.QMessageBox.information(self, 'Success', 'Fitness records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save fitness records.')
        
        time3 = str(os.times())
        sports3 = str(self.ui.comboBox_6.currentText())
        duration3 = str(self.ui.comboBox_7.currentText())
        
        if profile.save_fitness_records(self.username, time3, sports3, duration3):
            QtWidgets.QMessageBox.information(self, 'Success', 'Fitness records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save fitness records.')
            
        time4 = str(os.times())
        sports4 = str(self.ui.comboBox_8.currentText())
        duration4 = str(self.ui.comboBox_9.currentText())
        
        if profile.save_fitness_records(self.username, time4, sports4, duration4):
            QtWidgets.QMessageBox.information(self, 'Success', 'Fitness records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save fitness records.')
    
    def save_diet_records(self):
        time1 = str(os.times())
        food1 = str(self.ui.comboBox_10.currentText())
        weight1 = str(self.ui.comboBox_11.currentText())
        
        if profile.save_diet_records(self.username, time1, food1, weight1):
            QtWidgets.QMessageBox.information(self, 'Success', 'Diet records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save Diet records.')
            
        time2 = str(os.times())
        food2 = str(self.ui.comboBox_12.currentText())
        weight2 = str(self.ui.comboBox_13.currentText())
        
        if profile.save_diet_records(self.username, time2, food2, weight2):
            QtWidgets.QMessageBox.information(self, 'Success', 'Diet records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save Diet records.')
        
        time3 = str(os.times())
        food3 = str(self.ui.comboBox_14.currentText())
        weight3 = str(self.ui.comboBox_15.currentText())
        
        if profile.save_diet_records(self.username, time3, food3, weight3):
            QtWidgets.QMessageBox.information(self, 'Success', 'Diet records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save Diet records.')
            
        time4 = str(os.times())
        food4 = str(self.ui.comboBox_16.currentText())
        weight4 = str(self.ui.comboBox_17.currentText())
        
        if profile.save_diet_records(self.username, time4, food4, weight4):
            QtWidgets.QMessageBox.information(self, 'Success', 'Diet records saved successfully!')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to save Diet records.')

        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec())
