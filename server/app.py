from flask import Flask
from extensions import db  # Import the database instance
from routes import *  # Import routes to handle API requests

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Path to your SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
