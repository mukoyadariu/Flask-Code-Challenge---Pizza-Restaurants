from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

# Create a Flask app context
with app.app_context():
    # Create restaurants
    restaurant1 = Restaurant(name='Pizza Hut', address='123 Main St')
    restaurant2 = Restaurant(name='Domino\'s Pizza', address='456 Elm St')
    restaurant3 = Restaurant(name='Papa John\'s', address='789 Oak St')

    # Create pizzas
    pizza1 = Pizza(name='Pepperoni', ingredients='Pepperoni, cheese, tomato sauce')
    pizza2 = Pizza(name='Margherita', ingredients='Tomatoes, mozzarella cheese, basil')
    pizza3 = Pizza(name='Vegetarian', ingredients='Mushrooms, bell peppers, onions, olives')

    # Add objects to the session
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3])

    # Commit the changes to the database
    db.session.commit()

    # Create restaurant pizzas
    restaurant_pizza1 = RestaurantPizza(price=10.99, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    restaurant_pizza2 = RestaurantPizza(price=12.99, pizza_id=pizza2.id, restaurant_id=restaurant1.id)
    restaurant_pizza3 = RestaurantPizza(price=11.99, pizza_id=pizza2.id, restaurant_id=restaurant2.id)
    restaurant_pizza4 = RestaurantPizza(price=9.99, pizza_id=pizza3.id, restaurant_id=restaurant2.id)
    restaurant_pizza5 = RestaurantPizza(price=13.99, pizza_id=pizza1.id, restaurant_id=restaurant3.id)
    restaurant_pizza6 = RestaurantPizza(price=14.99, pizza_id=pizza3.id, restaurant_id=restaurant3.id)

    # Add objects to the session
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3,
                        restaurant_pizza4, restaurant_pizza5, restaurant_pizza6])

    # Commit the changes to the database
    db.session.commit()

    print('Database seeded successfully.')
