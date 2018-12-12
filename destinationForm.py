from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class DestinationForm(FlaskForm):
    journeyName = StringField("Name this Journey", validators=[DataRequired(), Length(min=2, max=20)])
    busNumber = IntegerField("Select Bus Number", validators=[DataRequired(), NumberRange(min=2, max=975,
                                                                                          message="Invalid Bus Number")])
    journeyFrom = StringField("From", validators=[DataRequired()])
    journeyTo = StringField("To", validators=[DataRequired()])
    alertMe = IntegerField("Alert Me Before {?} Stops", validators=[DataRequired()])
    submit = SubmitField("Submit")


class FeedbackForm(FlaskForm):
    journeyName = StringField("Name this Journey", validators=[DataRequired(), Length(min=2, max=20)])
    busNumber = IntegerField("Select Bus Number", validators=[DataRequired(), NumberRange(min=2, max=975,
                                                                                          message="Invalid Bus Number")])
    journeyFrom = StringField("From", validators=[DataRequired()])
    journeyTo = StringField("To", validators=[DataRequired()])
    alertMe = IntegerField("Alert Me Before {?} Stops", validators=[DataRequired()])
    submit = SubmitField("Submit")



