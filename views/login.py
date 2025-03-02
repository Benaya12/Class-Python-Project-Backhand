from flask import request, jsonify 
from models.employees import Employee
class Login:
    def __init__(self, app):
        app.add_url_rule('/login', view_func=self.login, methods=['POST'])
    

    
    def login(self):
        data = request.json
        try:
            employee = Employee.query.filter_by(username=data['username']).first()
            if employee and employee.password == data['password']:
                return jsonify({'message': 'Login successful'}), 200
            else:
                return jsonify({'message': 'Login failed'}), 401
        except Exception as e:
            print("error login:", e)
            return jsonify({'message': 'Login failed'}), 500
        
        