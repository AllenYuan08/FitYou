"""
This module is responsible for the diet functionality.
"""
import sqlite3
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog

def search_diet(food_name, model, label_12):
    # 连接数据库
    conn = sqlite3.connect('./Database/Diet.db')
    cursor = conn.cursor()

    # 执行查询
    query = "SELECT * FROM Diet WHERE Name=?"
    cursor.execute(query, (food_name,))

    # 获取查询结果
    rows = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()
    
    # 检查结果
    if len(rows) == 0:
        search_result = "No results found"
    else:
        # 将结果转换为字典格式
        columns = [description[0] for description in cursor.description]
        result_dict = dict(zip(columns, rows[0]))
        search_result = result_dict
    
    model.clear()
    
    if isinstance(search_result, dict):
        text_to_display = [f"{key}: {value}" for key, value in search_result.items()]
        for item in text_to_display:
            model.appendRow(QStandardItem(item))
    elif isinstance(search_result, str):
        text_to_display = search_result
        model.appendRow(QStandardItem(search_result))
    else:
        model.appendRow(QStandardItem("Something went wrong. Please try again."))

    if isinstance(search_result, dict) and 'Fig' in search_result:
        # 加载图片
        pixmap = QPixmap(search_result['Fig'])
        label_12.setPixmap(pixmap.scaled(label_12.size(), Qt.KeepAspectRatio))
    elif isinstance(search_result, str):
        # 清除图片，可以选择显示文本
        label_12.clear()
        label_12.setText("No image to display.")
    else:
        # 清除内容
        label_12.clear()
        label_12.setText("Something went wrong. Please try again.")
        
def upload_food_image(ui, label_11):
    filepath, _ = QFileDialog.getOpenFileName(ui, "Please choose the image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        
    if filepath:  # 检查用户是否选择了文件
        # 检查图片格式
        if not filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            label_11.setText("Unsupported image format. Please choose a valid image file.")
            return

        # 加载图片并显示
        pixmap = QPixmap(filepath)
        if pixmap.isNull():  # 检查图片是否有效
            label_11.setText("Unable to load the image. Please try again.")
        else:
            label_11.setPixmap(pixmap.scaled(label_11.size(), Qt.KeepAspectRatio))
