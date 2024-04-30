"""
This file is used to create, search, get, etc. the element in database.
"""
import sqlite3


class DatabaseManager():
    def __init__(self):
        self.conn = None
        self.cur = None
    
    def connect(self, db_name):
        if self.conn:
            self.conn.close()
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        
    def create_table(self):
        """
        create the table in database
        
        you can copy the code from the Data.py
        """
        self.cur.execute('''CREATE TABLE IF NOT EXISTS items
                     (id INTEGER PRIMARY KEY, name TEXT)''')
        self.conn.commit()
    
    def insert_data(self):
        """
        insert data into the table
        
        """
        self.cur.execute("INSERT INTO items (id, name) VALUES (?, ?)", (id, name))
        self.conn.commit()
    
    def search_data(self):
        """
        search the data from the table
        
        """
        self.cur.execute("SELECT * FROM items WHERE name=?", (name,))
        return self.cur.fetchall()
    
    def get_data(self):
        """
        get the data from the table
        
        """
        self.cur.execute("SELECT * FROM items")
        return self.cur.fetchall()
    
    def update_data(self):
        """
        update the data in the table
        
        """
        self.cur.execute("UPDATE items SET name=? WHERE id=?", (name, id))
        self.conn.commit()
    
    def delete_data(self):
        """
        delete the data in the table
        
        """
        self.cur.execute("DELETE FROM items WHERE id=?", (id,))
        self.conn.commit()
    
    def close(self):
        """
        close the database
        
        """
        if self.conn:
            self.conn.close()
    
# Example usage
db_manager = DatabaseManager()

# Connect to the first database and perform operations
db_manager.connect('DietData.db')
db_manager.create_table()

# Connect to the second database and perform operations without needing to create a new instance
db_manager.connect('ExerciseData.db')
db_manager.create_table()
    
    