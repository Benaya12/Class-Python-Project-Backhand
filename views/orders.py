from flask import request, jsonify

class Orders:
    def __init__(self, app):
        app.add_url_rule('/orders', view_func=self.addOrder, methods=['POST'])
        app.add_url_rule('/orders', view_func=self.getOrders, methods=['GET'])
        app.add_url_rule('/orders', view_func=self.removeOrder, methods=['DELETE'])
        app.add_url_rule('/orders', view_func=self.editOrder, methods=['PUT'])
    
    def addOrder(self):
        pass

    def getOrders(self):
        pass

    def removeOrder(self):
        pass

    def editOrder(self):
        pass