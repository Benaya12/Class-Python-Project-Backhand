from flask import request, jsonify

from models import db
from models.employees import Employee

class EmployeeView:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/employee', 'get_employee', self.getEmployee, methods=['GET'])
        self.app.add_url_rule('/employee', 'add_employee', self.addEmployee, methods=['POST'])
        self.app.add_url_rule('/employee/<int:id>', 'remove_employee', self.removeEmployee, methods=['DELETE'])
        self.app.add_url_rule('/employee/<int:id>', 'edit_employee', self.editEmployee, methods=['PUT'])

    def getEmployee(self):
        employees = Employee.query.all()
        return jsonify([{
        'id': employee.id,
        'username': employee.username,
        'password': employee.password,
        'role_id': employee.role_id,
        'salary': employee.salary
    } for employee in employees])

    def addEmployee(self):
        data = request.json
        try:
            new_employee = Employee(
                username=data['username'],
                password=data['password'],
                role_id=data['role_id'],
                salary=data['salary']
            )
            db.session.add(new_employee)
            db.session.commit()
            return jsonify({'message': 'Employee added to database.'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to add employee', 'message': str(e)}), 500

    def removeEmployee(self, id):
        try:
            employee = Employee.query.get(id)
            if employee is None:
                return jsonify({'error': 'Employee not found'}), 404
            db.session.delete(employee)
            db.session.commit()
            return jsonify({'message': 'Employee removed from database.'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to remove employee', 'message': str(e)}), 500

    def editEmployee(self, id):
        data = request.json
        try:
            employee = Employee.query.get(id)
            if employee is None:
                return jsonify({'error': 'Employee not found'}), 404
            employee.username = data.get('username', employee.username)
            employee.password = data.get('password', employee.password)
            employee.role_id = data.get('role_id', employee.role_id)
            employee.salary = data.get('salary', employee.salary)
            db.session.commit()
            return jsonify({'message': 'Employee updated in database.'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to update employee', 'message': str(e)}), 500
