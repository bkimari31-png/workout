#  Workout Tracker API

##  Description

A RESTful API built with Flask that allows users to create workouts, manage exercises, and track workout details (sets, reps, duration).

---

## Tech Stack

* Flask
* SQLAlchemy
* Marshmallow
* SQLite

---

##  Setup

```bash
pipenv install
pipenv shell

export FLASK_APP=app.py   # Windows: set FLASK_APP=app.py

flask db migrate -m "init"
flask db upgrade
flask run
```

---

##  Endpoints

### Workouts

* GET /workouts
* GET /workouts/<id>
* POST /workouts
* DELETE /workouts/<id>

### Exercises

* GET /exercises
* GET /exercises/<id>
* POST /exercises
* DELETE /exercises/<id>

### Workout Exercises

* POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises

---

##  Example Request

```json
{
  "date": "2026-04-15",
  "duration_minutes": 60,
  "notes": "Evening workout"
}
```
