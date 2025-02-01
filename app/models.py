from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditorField
from sqlalchemy import Column, Integer, Text

db = SQLAlchemy()

class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)  # Use Text for database storage

    def __init__(self, question, answer, question_hi=None, question_bn=None):
        self.question = question
        self.answer = answer
    def get_question(self):
        """Method to retrieve the question in English or translated."""
        return self.question
