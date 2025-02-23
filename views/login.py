from flask import request, jsonify 

class Login:
    def __init__(self, app):
        app.add_url_rule('/login', view_func=self.login, methods=['POST'])
    
    def login(self):
        pass