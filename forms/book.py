from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Title')
    author = TextAreaField('Content')
    submit = SubmitField('Post')
