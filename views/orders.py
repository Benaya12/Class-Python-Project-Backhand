from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Using in-memory database for testing
db = SQLAlchemy(app)

# Define Order model
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)


class Orders:
    def __init__(self, app):
        app.add_url_rule('/orders', view_func=self.addOrder, methods=['POST'])
        app.add_url_rule('/orders', view_func=self.getOrders, methods=['GET'])
        app.add_url_rule('/orders/<int:order_id>', view_func=self.removeOrder, methods=['DELETE'])
        app.add_url_rule('/orders/<int:order_id>', view_func=self.editOrder, methods=['PUT'])
    
    def addOrder(self):
        data = request.json  # Parse the JSON data from the request body
        try:
            new_order = Order(
                table_id=data['table_id'],  
                price=data['price'],
                status=data['status'],
            )
            db.session.add(new_order)  # Add the new order to the database session
            db.session.commit()  # Commit the session to save in the database
            return jsonify({'message': 'Order added to database.'}), 201
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': 'Failed to add order', 'message': str(e)}), 500

    def getOrders(self):
        try:
            orders = db.session.query(Order).all()  # Get all orders from the database
            orders_list = []  # Create an empty list to store the orders
            for order in orders:
                # Append each order to the list as a dictionary
                orders_list.append({
                    'id': order.id,
                    'table_id': order.table_id,
                    'price': order.price,
                    'status': order.status,
                })
            return jsonify(orders_list), 200
        except Exception as e:
            return jsonify({'error': 'Failed to get orders', 'message': str(e)}), 500

    def removeOrder(self, order_id):
        try:
            # Find the order by ID
            order = db.session.query(Order).filter_by(id=order_id).first()
            if order:
                db.session.delete(order)  # Delete the order from the database session
                db.session.commit()  # Commit the transaction
                return jsonify({'message': 'Order deleted from database.'}), 200
            else:
                return jsonify({'error': 'Order not found'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to delete order', 'message': str(e)}), 500

    def editOrder(self, order_id):
        data = request.json
        try:
            order = db.session.query(Order).filter_by(id=order_id).first()  # Find the order by ID
            if order:
                if 'status' in data:
                    order.status = data['status']  # Update the status
                if 'price' in data:
                    order.price = data['price']  # Update the price
                db.session.commit()  # Commit the transaction
                return jsonify({'message': 'Order updated.'}), 200
            else:
                return jsonify({'error': 'Order not found'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to update order', 'message': str(e)}), 500


# Main block for running the Flask app and tests
if __name__ == '__main__':
    db.create_all()  # Create the database tables
    
    # Initialize the Orders class with Flask app
    Orders(app)
    
    # Test case
    with app.test_client() as client:
        # Test adding an order
        response = client.post('/orders', json={'table_id': 1, 'price': 15.5, 'status': 'pending'})
        assert response.status_code == 201  # Assert that the status code is 201 (created)
        assert response.json['message'] == 'Order added to database.'

        # Test getting all orders
        response = client.get('/orders')
        assert response.status_code == 200  # Assert that the status code is 200 (OK)
        assert len(response.json) == 1  # There should be one order in the database

        # Test editing an order
        order_id = response.json[0]['id']
        response = client.put(f'/orders/{order_id}', json={'status': 'completed', 'price': 20.0})
        assert response.status_code == 200
        assert response.json['message'] == 'Order updated.'

        # Test deleting an order
        response = client.delete(f'/orders/{order_id}')
        assert response.status_code == 200  # Assert that the status code is 200 (OK)
        assert response.json['message'] == 'Order deleted from database.'

        # Test getting orders after deletion (should be empty)
        response = client.get('/orders')
        assert response.status_code == 200
        assert len(response.json) == 0  # There should be no orders left in the database
