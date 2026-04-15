from flask import Flask
from flask_migrate import Migrate

from models import db

# Import blueprints
from routes.workout_routes import workout_bp
from routes.exercise_routes import exercise_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(workout_bp)
app.register_blueprint(exercise_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)