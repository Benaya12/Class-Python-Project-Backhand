from flask import request, jsonify
from models import db
from models.foodType import FoodType

class FoodTypeView:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/foodtype', 'get_food_type', self.getFoodType, methods=['GET'])
        self.app.add_url_rule('/foodtype', 'add_food_type', self.addFoodType, methods=['POST'])
        self.app.add_url_rule('/foodtype/<int:id>', 'delete_food_type', self.deleteFoodType, methods=['DELETE'])
        self.app.add_url_rule('/foodtype/<int:id>', 'update_food_type', self.updateFoodType, methods=['PUT'])

    def getFoodType(self):
        food_types = FoodType.query.all()
        return jsonify([{
            'id': food_type.id,
            'name': food_type.name
        } for food_type in food_types])

    def addFoodType(self):
        data = request.get_json()
        new_food_type = FoodType(name=data['name'])
        db.session.add(new_food_type)
        db.session.commit()
        return jsonify({'message': 'Food type added successfully'}), 201

    def deleteFoodType(self, id):
        food_type = FoodType.query.get_or_404(id)
        db.session.delete(food_type)
        db.session.commit()
        return jsonify({'message': 'Food type deleted successfully'}), 200

    def updateFoodType(self, id):
        data = request.get_json()
        food_type = FoodType.query.get_or_404(id)
        food_type.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Food type updated successfully'}), 200