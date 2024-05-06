"""
This module is responsible for the profile in functionality.
"""
import sqlite3

def get_user_info(username, list_widget_username, list_widget_age, list_widget_sex, list_widget_weight):
    conn = sqlite3.connect('./Database/User.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT Name, Age, Sex, Weight FROM User WHERE username = ?", (username,))
    result = cursor.fetchone()

    # 清空列表并显示新数据
    list_widget_username.clear()
    list_widget_age.clear()
    list_widget_sex.clear()
    list_widget_weight.clear()
    
    if result:
        list_widget_username.addItem(result[0] or "No data")
        list_widget_age.addItem(result[1] or "No data")
        list_widget_sex.addItem(result[2] or "No data")
        list_widget_weight.addItem(result[3] or "No data")
        
    else:
        list_widget_username.addItem("No data")
        list_widget_age.addItem("No data")
        list_widget_sex.addItem("No data")
        list_widget_weight.addItem("No data")

    conn.close()
    
def save_user_info(username, name, age, sex, weight):
    try:
        conn = sqlite3.connect('./Database/User.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE User SET Name = ?, Age = ?, Sex = ?, Weight = ?
            WHERE username = ?""",
            (name, age, sex, weight, username))
        conn.commit()
        updated_rows = cursor.rowcount  # 获取受影响的行数
        conn.close()
        return updated_rows > 0  # 如果有行被更新，则返回True
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
        return False
    
def save_fitness_records(username, time, sports, duration):
    # 构建数据库文件名
    db_filename = f"{username}_Fitness_Records.db"

    # 连接到数据库
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Fitness_Records (
            id INTEGER PRIMARY KEY,
            Username TEXT,
            Time TEXT,
            Sports TEXT,
            Duration TEXT
        )
    ''')
    # 插入数据，这里假设我们总是添加新数据
    cursor.execute('''
        INSERT INTO Fitness_Records (Username, Time, Sports, Duration) 
        VALUES (?, ?, ?, ?)
    ''', (username, time, sports, duration))

    # 提交事务
    conn.commit()

    # 关闭数据库连接
    conn.close()

    print(f"Data successfully written to {db_filename}")
    
    return True

def save_diet_records(username, time, food, weight):
    # 构建数据库文件名
    db_filename = f"{username}_Diet_Records.db"

    # 连接到数据库
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Diet_Records (
            id INTEGER PRIMARY KEY,
            Username TEXT,
            Time TEXT,
            Food TEXT,
            Weight TEXT
        )
    ''')
    # 插入数据，这里假设我们总是添加新数据
    cursor.execute('''
        INSERT INTO Diet_Records (Username, Time, Food, Weight) 
        VALUES (?, ?, ?, ?)
    ''', (username, time, food, weight))

    # 提交事务
    conn.commit()

    # 关闭数据库连接
    conn.close()

    print(f"Data successfully written to {db_filename}")
    
    return True
