from app import create_app,db
import json
from flask import redirect,url_for,jsonify


app = create_app()
with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return redirect(url_for('api_routes'))

@app.route('/api/', methods=['GET'])
def api_routes():
    routes_info = {
        "GET /api/faqs": {
            "description": "Fetch all FAQs in the default language (English). If questions/answers are in another language, they are translated into English.",
            "response_example": [
                {
                    "id": 1,
                    "question": "Why is my account associated with a region?",
                    "answer": "Your account is associated with a region (or territory) in the Terms of Service so that we can determine several things..."
                },
                {
                    "id": 2,
                    "question": "Why is my account associated with a region?",
                    "answer": "Your account is associated with a region (or territory) in the Terms of Service so that we can determine several things..."
                }
            ]
        },
        "GET /api/faqs?lang={lang}": {
            "description": "Fetch all FAQs in the specified language.",
            "response_example": [
                {
                    "id": 1,
                    "question": "నా ఖాతా ఒక ప్రాంతంతో ఎందుకు సంబంధం కలిగి ఉంది?",
                    "answer": "మీ ఖాతా సేవా నిబంధనలలో ఒక ప్రాంతంతో (లేదా భూభాగం) సంబంధం కలిగి ఉంది..."
                },
                {
                    "id": 2,
                    "question": "నా ఖాతా ఒక ప్రాంతంతో ఎందుకు సంబంధం కలిగి ఉంది?",
                    "answer": "మీ ఖాతా సేవా నిబంధనలలో ఒక ప్రాంతంతో (లేదా భూభాగం) సంబంధం కలిగి ఉంది..."
                }
            ]
        },
        "POST /api/faqs": {
            "description": "Create a new FAQ.",
            "request_example": {
                "question": "What are parameters?",
                "answer": "lang is the parameter"
            },
            "response_example": {
                "message": "FAQ added successfully"
            }
        },
        "GET /api/faqs/add_faq": {
            "description": "View the form to add a new FAQ without WYSIWYG formatting.",
            "view_example": "/static/add_faq.png"
        },
        "GET /api/faqs/get_faqs_WYSIWYG": {
            "description": "View the FAQs in WYSIWYG format.",
            "view_example": "/static/get_faqs_with_WYSIWYG.png"
        }
    }
    
    return jsonify(routes_info)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
