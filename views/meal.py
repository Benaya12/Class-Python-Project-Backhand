from flask import request, jsonify

from models import db


class Meal:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/meal', 'get_meal', self.getMeals, methods=['GET'])
        self.app.add_url_rule('/meal', 'add_meal', self.addMeal, methods=['POST'])
        self.app.add_url_rule('/meal', 'remove_meal', self.removeMeal, methods=['DELETE'])
        self.app.add_url_rule('/meal', 'edit_meal', self.editMeal, methods=['PUT'])
    
    def addMeal(self):
        data = request.json  # Parse the JSON data from the request body
        try:
            new_meal = Meal(
                name=data['name'],  # Set the title of the new meal
                price=data['price'],
                image=data['image'],
                description=data['description'],
                foodType=data['foodType']
            )
            db.session.add(new_meal)  # Add the new meal to the database session
            db.session.commit()  # Commit the session to save in the database
            return jsonify({'message': 'Meal added to database.'}), 201
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': 'Failed to add meal', 'message': str(e)}), 500


    def getMeals(self):
        try:
            meals = Meal.query.all()  # Get all the meals from the database
            meals_list = [{
                'id': meal.id,
                'name': meal.name,
                'price': meal.price,
                'image': meal.image,
                'description': meal.description,
                'foodType': meal.foodType
            } for meal in meals]  # Create a list of meal dictionaries
            return jsonify({
                'message': 'Meals retrieved successfully',
                'meals': meals_list
            }), 200
        except Exception as e:
            return jsonify({
                'error': 'Failed to retrieve meals',
                'message': str(e)
            }), 500

    def removeMeal(self):
        pass

    def editMeal(self):
        pass




