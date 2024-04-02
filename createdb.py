from app import db,app
from app import Todo

# Create the database tables
with app.app_context():
    db.create_all()
