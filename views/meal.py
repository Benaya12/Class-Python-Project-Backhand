from flask import request, jsonify

from models import db
from models.meal import Meal
from models.foodType import FoodType

class MealView:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/meal', 'get_meal', self.get_meals, methods=['GET'])
        self.app.add_url_rule('/meal', 'add_meal', self.add_meal, methods=['POST'])
        self.app.add_url_rule('/meal', 'remove_meal', self.remove_meal, methods=['DELETE'])
        self.app.add_url_rule('/meal', 'edit_meal', self.edit_meal, methods=['PUT'])
    
    def add_meal(self):
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



    def get_meals(self):
        try:
            meals = Meal.query.all()  # Get all the meals from the database

            meals_list = [{
                'id': meal.id,
                'name': meal.name,
                'price': meal.price,
                'image': meal.image,
                'description': meal.description,
                'foodType': FoodType.query.filter_by(id=meal.foodType).first().name
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

    def remove_meal(self):
        data = request.json
        try:
            meal = db.session.get(Meal, data['id'])  # Get the meal by ID
            if not meal:
                return jsonify({'error': 'Meal not found'}), 404
            db.session.delete(meal)  # Delete the meal
            db.session.commit()  # Commit the changes
            return jsonify({'message': 'Meal deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': 'Failed to delete meal', 'message': str(e)}), 500

    def edit_meal(self):
        data = request.json
        try:
            meal = db.session.get(Meal, data['id'])  # Get the meal by ID
            if not meal:
                return jsonify({'error': 'Meal not found'}), 404
            meal.name = data['name']  # Set the title of the new meal
            meal.price = data['price']
            meal.image = data['image']
            meal.description = data['description']
            meal.foodType = data['foodType']
            db.session.commit()  # Commit the changes
            return jsonify({'message': 'Meal updated successfully'}), 200
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': 'Failed to update meal', 'message': str(e)}), 500









