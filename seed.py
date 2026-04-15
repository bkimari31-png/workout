from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():

    print("Seeding database...")

    db.drop_all()
    db.create_all()

    # Exercises
    e1 = Exercise(name="Push Up", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Squat", category="Strength", equipment_needed=False)
    e3 = Exercise(name="Running", category="Cardio", equipment_needed=False)

    # Workout
    w1 = Workout(date=date.today(), duration_minutes=45, notes="Morning workout")

    db.session.add_all([e1, e2, e3, w1])
    db.session.commit()

    # Join entries
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=12, sets=3)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=e3.id, duration_seconds=600)

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Database seeded!")