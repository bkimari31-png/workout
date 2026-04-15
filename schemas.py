from marshmallow import Schema, fields, validates, ValidationError


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    exercise_id = fields.Int(required=True)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates('name')
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True)