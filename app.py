from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
# db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants]
    return jsonify(restaurant_list)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        }
        return jsonify(restaurant_data)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Implement other routes: DELETE /restaurants/:id, GET /pizzas, POST /restaurant_pizzas

if __name__ == '__main__':
    app.run(debug=True)