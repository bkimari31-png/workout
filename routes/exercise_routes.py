from flask import Blueprint, request, jsonify

from models import db, Exercise
from schemas import ExerciseSchema

exercise_bp = Blueprint('exercise_bp', __name__)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


# GET ALL EXERCISES

@exercise_bp.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


# GET ONE EXERCISE

@exercise_bp.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    return exercise_schema.dump(exercise), 200


# CREATE EXERCISE

@exercise_bp.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()

    try:
        exercise = Exercise(**data)

        db.session.add(exercise)
        db.session.commit()

        return exercise_schema.dump(exercise), 201

    except Exception as e:
        return {"error": str(e)}, 400


# DELETE EXERCISE

@exercise_bp.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    db.session.delete(exercise)
    db.session.commit()

    return {}, 204