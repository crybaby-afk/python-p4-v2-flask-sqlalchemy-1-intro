from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Define metadata for database schema
metadata = MetaData()

# Initialize SQLAlchemy
db = SQLAlchemy(metadata=metadata)

# Define a database model (Pet)
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
