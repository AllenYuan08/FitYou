"""
This module is responsible for the fitness functionality.
"""
from PyQt5 import QtCore

from database import DatabaseManager

class Fitness(QtCore):
    def __init__(self):
        pass
    
    def get_exercise_img_show(self):
        """
        get the image from the database and show it, by using the function provided in the database.py
        the image will be shown in the UI
        The data stored in the database will be the path of the image
        you need to display the image by opening the image file
        
        return true if the image is shown
        """
        """
        find the pictures and show it.
        """
        imagePath = self.db_manager.search_data('image_path')  # call
        if imagePath:
            # open and show the pictures.
            print(f"from {imagePath} show")
            return True
        else:
            print("not found.")
            return False
    
    def get_exercise_video(self):
        """
        After user click the exercise video (a signal), the video will be shown
        same as the image, the path of video will be stored in the database
        you need to display the video by opening the video file
        
        return true if the video is shown
        """
        """
        from the vidoe path and sow it. 
        """
        videoPath = self.db_manager.search_data('video_path')  # call
        if videoPath:
            # open and play the video.
            print(f"from {videoPath} play")
            return True
        else:
            print("not found")
            return False
    
    def get_exercise_data(self):
        """
        you need to get the basic data of specific exercise choosen by the user
        from the database using the function provided in the database.py
        
        return the basic data of the exercise using a dictionary, 
        like {'name': 'pushup', 'calories': 100, 'time': 10}
        """
    
        """
        Get basic data of a specific exercise chosen by the user from the database.
        """
        exerciseData = self.db_manager.get_data('exercise_name')  # Simulated function call
        if exerciseData:
            # Assuming exerciseData is a dictionary like {'name': 'pushup', 'calories': 100, 'time': 10}
            print(f"Exercise data retrieved: {exerciseData}")
            return exerciseData
        else:
            print("No data found for the specified exercise.")
            return {}
    
    def calculate_static(self):
        """
        you need to calculate the statics of the exercise after users input like time, weight, etc.
        based on the basic data of the exercise you get from the get_exercise_data function
        
        return the statics of the exercise, 
        like the overall data of the exercise after the user input based on the exercise data
        store it as a dictionary, 
        like {'calories': 100, 'time': 10}
        """
        """
        Calculate the statistics of the exercise based on user input.
        """
        exerciseData = self.get_exercise_data()  # Assuming this returns a dictionary with necessary data
        if not exerciseData:
            print("Exercise data is required for calculation.")
            return {}
        
        # Example calculation, adjust according to your application's logic
        calculatedStatics = {
            'calories': exerciseData.get('calories', 0) * userInput.get('duration', 1),
            'time': exerciseData.get('time', 0) + userInput.get('extra_time', 0)
        }
        
        print(f"Calculated statics: {calculatedStatics}")
        return calculatedStatics