"""
This module is responsible for the log in functionality.
"""
import sqlite3
from PySide6 import QtWidgets
import pandas as pd

def sign_up(name, phnum, username, password, confirm_password):
    if password != confirm_password:
        # 如果密码不匹配，显示错误消息
        return False
    
    # 数据库操作
    conn = sqlite3.connect('./Database/User.db')
    c = conn.cursor()
    # c.execute('CREATE TABLE IF NOT EXISTS Data (Username TEXT, Password TEXT, Ph No. TEXT, Name TEXT)')
    c.execute('INSERT INTO User (Username, Password, Ph_No, Name) VALUES (?, ?, ?, ?)', (username, password, phnum, name))
    conn.commit()
    conn.close()
    
    return True

def validate_login(username, password):
    connection = sqlite3.connect("./Database/User.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def create_databases_for_user(username, excel_file_path, sheet_name):
    # 读取 Excel 文件
    xls = pd.ExcelFile(excel_file_path)

    # 为每个工作表创建一个数据库
    # 生成数据库名称
    if sheet_name == "Fitness_Records":
        folder_name = "fitness"
    elif sheet_name == "Diet_Records":
        folder_name = "diet"
    db_name = f"./User_database/{folder_name}/{username}_{sheet_name}.db"
    
    # 读取工作表内容
    df = pd.read_excel(xls)
    
    # 连接到 SQLite 数据库，如果不存在会自动创建
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 创建表格，假设工作表名就是要创建的表名
    # 注意：这里假设 DataFrame 中的列名和数据类型都适合直接用来创建 SQL 表
    # 在实际应用中可能需要对这部分进行更精细的控制
    df.to_sql(sheet_name, conn, if_exists='replace', index=False)

    # 关闭数据库连接
    conn.close()
    print(f"Database {db_name} created and populated with data from {sheet_name}.")

