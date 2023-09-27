# Pizza Restaurants Flask API

## Overview

This project is a Flask-based API for managing pizza restaurants and their menus. It provides endpoints for creating, reading, updating, and deleting restaurants, pizzas, and their associations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Sample Requests](#sample-requests)
- [Models](#models)
- [Validations](#validations)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for managing dependencies)
- Flask and other required packages (see [Pipfile](Pipfile))

## Getting Started

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Flask-Code-Challenge-Pizza-Restaurants
   ```

3. Install project dependencies using Pipenv:

   ```bash
   pipenv install
   ```

### Running the Application

1. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

2. Set up the Flask app:

   ```bash
   export FLASK_APP=api/app.py
   ```

3. Run the Flask development server:

   ```bash
   flask run
   ```

The server will start running at `http://localhost:5000`.

## Usage

### API Endpoints

The following API endpoints are available:

- `GET /restaurants`: Retrieve a list of all restaurants.
- `GET /restaurants/<id>`: Retrieve a specific restaurant by ID.
- `DELETE /restaurants/<id>`: Delete a restaurant by ID.
- `GET /pizzas`: Retrieve a list of all pizzas.
- `POST /restaurant_pizzas`: Create a new RestaurantPizza association.

### Sample Requests

Here are some sample requests you can make to the API:

#### Retrieve all restaurants:

```http
GET /restaurants
```

#### Retrieve a specific restaurant:

```http
GET /restaurants/<id>
```

#### Delete a restaurant:

```http
DELETE /restaurants/<id>
```

#### Retrieve all pizzas:

```http
GET /pizzas
```

#### Create a new RestaurantPizza association:

```http
POST /restaurant_pizzas
```

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

## Models

The project uses the following models:

- Restaurant
- Pizza
- RestaurantPizza (Association model)

## Validations

- RestaurantPizza must have a price between 1 and 30.
- Restaurant must have a name less than 50 characters in length and must have a unique name.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Dennis Darius Mukoya**
