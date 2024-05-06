import pandas as pd
from sqlalchemy import create_engine
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.modules.utils import get_Project_path



def read_excel_data(filepath):
    """
    读取Excel文件数据。
    :param filepath: Excel文件的路径。
    :return: DataFrame。
    """
    return pd.read_excel(filepath)

def create_database_engine(db_name='your_database_name.db'):
    """
    创建数据库引擎。
    :param db_name: 数据库文件名。
    :return: SQLAlchemy Engine 实例。
    """
    return create_engine(f'sqlite:///{db_name}')

def export_data_to_sql(df, engine, table_name):
    """
    将数据导入SQL数据库。
    :param df: DataFrame，包含要导入的数据。
    :param engine: SQLAlchemy Engine 实例。
    :param table_name: 数据库中的表名。
    :return: None。
    """
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"数据已成功导入到数据库表 {table_name} 中！")

if __name__ == '__main__':
    # 示例使用
    abs_path = get_Project_path()
    filepath = abs_path + '/Data/Database_files/User.xlsx'  # 将此路径替换为您的文件路径
    db_name = abs_path + '/Database/User.db'  # 您可以自定义数据库名称
    table_name = 'User'  # 自定义表名称

    # 读取数据
    df = read_excel_data(filepath)

    # 创建数据库引擎
    engine = create_database_engine(db_name)

    # 导出数据到SQL
    export_data_to_sql(df, engine, table_name)
