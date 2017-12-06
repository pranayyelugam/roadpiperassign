from flask_wtf import FlaskForm
from wtforms import IntegerField ,FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    Truck_number = IntegerField('Truck_number', validators=[DataRequired()])
    latitude = FloatField('latitude', validators=[DataRequired()])
    longitude = FloatField('longitude', validators=[DataRequired()])