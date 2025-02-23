from flask import request, jsonify

class Menu:
    def __init__(self, app):
        app.add_url_rule('/menu', view_func=self.addMeal, methods=['POST'])
        app.add_url_rule('/menu', view_func=self.deleteMeal, methods=['DELETE'])
        app.add_url_rule('/menu', view_func=self.editMeal, methods=['PUT'])
    
    def addMeal(self):
        pass

    def deleteMeal(self):
        pass

    def editMeal(self):
        pass