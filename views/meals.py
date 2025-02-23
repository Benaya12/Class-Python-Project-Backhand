from flask import request, jsonify

class Meals:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/meals', 'get_meals', self.getMeals, methods=['GET'])
        self.app.add_url_rule('/meals', 'add_meal', self.addMeal, methods=['POST'])
        self.app.add_url_rule('/meals', 'remove_meal', self.removeMeal, methods=['DELETE'])
        self.app.add_url_rule('/meals', 'edit_meal', self.editMeal, methods=['PUT'])
    
    def addMeal(self):
        pass

    def getMeals(self):
        pass

    def removeMeal(self):
        pass

    def editMeal(self):
        pass