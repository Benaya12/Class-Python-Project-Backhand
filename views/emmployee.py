from flask import request, jsonify

from models import db
from models.employees import Employee

class EmployeeView:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/employee', 'get_employee', self.addEmployee, methods=['GET'])
        # self.app.add_url_rule('/employee', 'add_employee', self.addMeal, methods=['POST'])
        # self.app.add_url_rule('/employee', 'remove_employee', self.removeMeal, methods=['DELETE'])
        # self.app.add_url_rule('/employee', 'edit_employee', self.editMeal, methods=['PUT'])

    def addEmployee(self, app):
        data = request.json  # Parse the JSON data from the request body
        try:
            new_employee = Employee(
                username=data['username'],  # Set the title of the new meal
                password=data['password'],
                imagerole_id=data['role_id']
            )
            db.session.add(new_employee)  # Add the new meal to the database session
            db.session.commit()  # Commit the session to save in the database
            return jsonify({'message': 'employee added to database.'}), 201
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': 'Failed to add employee', 'message': str(e)}), 500