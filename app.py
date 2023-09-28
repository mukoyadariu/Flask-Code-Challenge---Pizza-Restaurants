from flask import Flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
# postgresql://pizza_221n_user:4v5PMJdMNKB2aUAOasNg5B2po2rGIF7D@dpg-ckaihn6gtj9c738sl2s0-a.oregon-postgres.render.com/pizza_221n


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=8006)