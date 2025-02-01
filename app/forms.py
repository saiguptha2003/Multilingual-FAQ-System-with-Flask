# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class FAQForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    answer = CKEditorField('Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')
