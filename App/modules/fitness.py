"""
This module is responsible for the fitness functionality.
"""
import sqlite3
from PySide6.QtWidgets import QLabel, QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Qt

   
def search_fitness(search_fitness_name, textEdit, label_10):
    # 连接数据库
    conn = sqlite3.connect('./Database/Fitness.db')
    cursor = conn.cursor()

    # 执行查询
    query = "SELECT * FROM Fitness WHERE Name=?"
    cursor.execute(query, (search_fitness_name,))

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
        
    if isinstance(search_result, dict):
        text_to_display = "\n\n".join(f"{key}: {value}" for key, value in search_result.items())
    elif isinstance(search_result, str):
        text_to_display = search_result
    else:
        text_to_display = "Something went wrong. Please try again."

    textEdit.setText(text_to_display)
    
    if isinstance(search_result, dict) and 'Fig' in search_result:
        # 加载图片
        pixmap = QPixmap(search_result['Fig'])
        label_10.setPixmap(pixmap.scaled(label_10.size(), Qt.KeepAspectRatio))
    elif isinstance(search_result, str):
        # 清除图片，可以选择显示文本
        label_10.clear()
        label_10.setText("No image to display.")
    else:
        # 清除内容
        label_10.clear()
        label_10.setText("Something went wrong. Please try again.")
