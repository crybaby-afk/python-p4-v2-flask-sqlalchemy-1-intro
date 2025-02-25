from flask import Flask
from flask_migrate import Migrate
from models import db

# Create a Flask application
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
