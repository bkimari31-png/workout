from flask import Blueprint, request, jsonify

from datetime import datetime
from models import db, Workout, WorkoutExercise
from schemas import WorkoutSchema

workout_bp = Blueprint('workout_bp', __name__)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

# GET ALL WORKOUTS

@workout_bp.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200


# GET ONE WORKOUT

@workout_bp.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return {"error": "Workout not found"}, 404

    return workout_schema.dump(workout), 200

# CREATE WORKOUT


@workout_bp.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()

    try:
        workout = Workout(
            date=datetime.strptime(data['date'], "%Y-%m-%d").date(),  # ✅ FIX
            duration_minutes=data['duration_minutes'],
            notes=data.get('notes')
        )

        db.session.add(workout)
        db.session.commit()

        return workout_schema.dump(workout), 201

    except Exception as e:
        return {"error": str(e)}, 400


# DELETE WORKOUT

@workout_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return {"error": "Workout not found"}, 404

    db.session.delete(workout)
    db.session.commit()

    return {}, 204


# ADD EXERCISE TO WORKOUT

@workout_bp.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json()

    try:
        new_entry = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get('reps'),
            sets=data.get('sets'),
            duration_seconds=data.get('duration_seconds')
        )

        db.session.add(new_entry)
        db.session.commit()

        return {"message": "Exercise added to workout"}, 201

    except Exception as e:
        return {"error": str(e)}, 400