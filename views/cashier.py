from flask import request, jsonify 

class Cashier:
    def __init__(self, app):
        app.add_url_rule('/cashier', view_func=self.display_cashier, methods=['GET'])

    def display_cashier(self):
        pass