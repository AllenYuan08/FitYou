"""
This module is responsible for the profile in functionality.
"""
from PyQt5 import QtCore

class Profile(QtCore):
    def __init__(self):
        pass
    
    def get_user_info(self):
        """
        get the user information from the database
        you need to get the user information from the database using the function provided in the database.py
        
        return the user information using a dictionary, 
        like {'Username': 'John', 'Ages': 20, 'Sex': Male, 'weight': 70}
        """
        pass
    
    def save_user_info(self, user_info):
        """
        store the user information to the database
        you need to store the user information to the database using the function provided in the database.py
        
        user_info is a dictionary, like {'Username': 'John', 'Ages': 20, 'Sex': Male, 'weight': 70}
        store them in the database with corresponding place
        """
        pass
    
    def save_fitness_records(self, fitness_records):
        """
        store the fitness records to the database
        you need to store the fitness records to the database using the function provided in the database.py
        
        fitness_records is a dictionary, like {'date': '2021-01-01', 'exercise': 'pushup', 'time': 10}
        store them in the database with corresponding place
        
        date can be get from a function utils.userful_utils.get_date()
        """
        pass
    
    def save_diet_records(self, diet_records):
        """
        store the diet records to the database
        you need to store the diet records to the database using the function provided in the database.py
        
        diet_records is a dictionary, like {'date': '2021-01-01', 'food': 'apple', 'calories': 100}
        store them in the database with corresponding place
        
        date can be get from a function utils.userful_utils.get_date()
        """
        pass
    
    