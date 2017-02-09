from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class SentimentForm(Form):
    sentiment = TextAreaField('sentiment', validators=[DataRequired()])
