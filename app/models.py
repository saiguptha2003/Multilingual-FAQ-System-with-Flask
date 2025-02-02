from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditorField
from sqlalchemy import Column, Integer, Text
from flask import current_app as app, json
import requests
from bs4 import BeautifulSoup

import json
import logging
from .config import Config
from .translations import sign_request
db = SQLAlchemy()
AWS_ACCESS_KEY = Config.AWS_ACCESS_KEY
AWS_SECRET_KEY = Config.AWS_SECRET_KEY
AWS_REGION = Config.AWS_REGION
SERVICE = Config.SERVICE
API_URL = Config.API_URL

class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __init__(self, question, answer, question_hi=None, question_bn=None):
        self.question = question
        self.answer = answer
    def get_question(self):

        return self.question
        
    def translate_faq(self, lang):
            payload = json.dumps({
                "question": self.question,
                "answer": BeautifulSoup(self.answer, "html.parser").get_text(),
                "target_language": lang
            })

            signed_headers = sign_request("POST", API_URL, payload, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, SERVICE)

            try:
                response_faq = requests.post(API_URL, data=payload, headers=signed_headers)
                app.logger.info(f"API Response Code: {response_faq.status_code}")

                if response_faq.status_code == 200:
                    response_data = response_faq.json()
                    response_data = json.loads(response_data["body"])
                    translated_question = response_data.get("translated_text_question", {}).get("TranslatedText", self.question)
                    translated_answer = response_data.get("translated_text_answer", {}).get("TranslatedText", self.answer)

                    app.logger.info(f"Translated Question: {translated_question}")
                    app.logger.info(f"Translated Answer: {translated_answer}")

                    return {
                        "id": self.id,
                        "question": translated_question,
                        "answer": translated_answer
                    }
                else:
                    return {
                        "question": self.question,
                        "answer": BeautifulSoup(self.answer, "html.parser").get_text(),
                        "response": response_faq.text
                    }

            except requests.exceptions.RequestException as e:
                app.logger.error(f"Request failed: {e}")

                return {
                    "question": self.question,
                    "answer": BeautifulSoup(self.answer, "html.parser").get_text(),
                    "response": str(e)
                }
