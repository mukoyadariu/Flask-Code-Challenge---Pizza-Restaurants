# Create a function to add sample data to the database
def populate_database():
    # Check if the restaurant already exists
    existing_restaurant = Restaurant.query.filter_by(name="Dominion Pizza").first()
    
    if not existing_restaurant:
        # Create sample restaurant if it doesn't exist
        restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        db.session.add(restaurant1)

    # Create sample restaurants
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create sample pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add the records to the database
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)

    # Commit the changes to the database
    db.session.commit()
