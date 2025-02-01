# Multilingual FAQ System with Flask

## This is a python based flask Application 
## flask is a python backend framework


## Features
##### FAQ Management: Add FAQ entries.
##### Multilingual Support: Automatically translate FAQ questions and## answers into multiple languages.
##### SQLAlchemy Integration: Store FAQ data in a relational database using SQLAlchemy.
##### REST API: Expose APIs to fetch FAQ data and handle translations.


## Technologies Used
### Flask: A lightweight WSGI web application framework for Python.
##### SQLAlchemy: ORM for database management.
##### Requests: For making HTTP requests to translation APIs.
##### JSON: Data exchange format for translating FAQ content.
##### Redis: Data caching server side
##### Docker : Container based development

## Installation
### Clone The Repository 

```bash
git clone https://github.com/saiguptha2003/Multilingual-FAQ-System-with-Flask.git
cd Multilingual-FAQ-System-with-Flask
```

### Local Execution
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/MacOS
source venv/bin/activate

pip install -r requirements.txt

```

### Set up the environment variables:

##### API_URL: The URL for your translation API.
##### AWS_ACCESS_KEY: Your AWS access key for the translation service.
##### AWS_SECRET_KEY: Your AWS secret key for the translation service.
##### AWS_REGION: The AWS region for the service.
##### SERVICE: The AWS service you are using for translation.

```bash 
python app.py

```

### Docker Compose Execution

```bash
docker-compose up --build -d
```

## API Endpoints

##### GET api/faqs: Fetch all FAQs.
#####  POST api/faqs: Create a new FAQ.
##### FORM apifaqs/add_faq: Form for adding faq
##### GET api/faqs?lang=bn: Fetch All FAQs in given language 

## Database Schema
#### The application uses SQLAlchemy for database interaction. The FAQ table schema is as follows:

##### id: Primary key (integer).
##### question: The FAQ question (string).
##### answer: The FAQ answer (text)

## Requests and Response
### GET api/faqs/?lang=te: Fetch all FAQs.
#### URL
```json
http://localhost:5000/api/faqs?lang=te
```
#### Response:
```json
[
    {
        "answer": "మీ ఖాతా సేవా నిబంధనలలో ఒక ప్రాంతంతో (లేదా భూభాగం) సంబంధం కలిగి ఉంది, తద్వారా మేము అనేక విషయాలను గుర్తించగలము:\r\n\r\nసేవలను అందించే Google అనుబంధ సంస్థ, మీ సమాచారాన్ని ప్రాసెస్ చేస్తుంది మరియు వర్తించే గోప్యతా చట్టాలకు అనుగుణంగా బాధ్యత వహిస్తుంది. సాధారణంగా, గూగుల్ తన వినియోగదారుల సేవలను రెండు కంపెనీల ద్వారా అందిస్తుంది:\r\nగూగుల్ ఐర్లాండ్ లిమిటెడ్, మీరు యూరోపియన్ ఎకనామిక్ ఏరియా (EU దేశాలు ప్లస్ ఐస్లాండ్, లిచ్టెన్స్టెయిన్ మరియు నార్వే) లేదా స్విట్జర్లాండ్లో ఉన్నట్లయితే",
        "id": 1,
        "question": "నా ఖాతా ఒక ప్రాంతంతో ఎందుకు సంబంధం కలిగి ఉంది?"
    },
    {
        "answer": "మీ ఖాతా సేవా నిబంధనలలో ఒక ప్రాంతంతో (లేదా భూభాగం) సంబంధం కలిగి ఉంది, తద్వారా మేము అనేక విషయాలను గుర్తించగలము:\r\n\r\nసేవలను అందించే Google అనుబంధ సంస్థ, మీ సమాచారాన్ని ప్రాసెస్ చేస్తుంది మరియు వర్తించే గోప్యతా చట్టాలకు అనుగుణంగా బాధ్యత వహిస్తుంది. సాధారణంగా, గూగుల్ తన వినియోగదారుల సేవలను రెండు కంపెనీల ద్వారా అందిస్తుంది:\r\nగూగుల్ ఐర్లాండ్ లిమిటెడ్, మీరు యూరోపియన్ ఎకనామిక్ ఏరియా (EU దేశాలు ప్లస్ ఐస్లాండ్, లిచ్టెన్స్టెయిన్ మరియు నార్వే) లేదా స్విట్జర్లాండ్లో ఉన్నట్లయితే",
        "id": 2,
        "question": "నా ఖాతా ఒక ప్రాంతంతో ఎందుకు సంబంధం కలిగి ఉంది?"
    }
]

```


### GET api/faqs: Fetch all FAQs.
#### URL
```json
http://localhost:5000/api/faqs/
```
#### Response:
```json
[
    {
        "answer": "Your account is associated with a region (or territory) in the Terms of Service so that we can determine several things:\r\n\r\nThe Google affiliate that provides the services, that processes your information, and that is responsible for complying with applicable privacy laws. Generally, Google offers its consumer services through either of two companies:\r\nGoogle Ireland Limited, if you’re located in the European Economic Area (EU countries plus Iceland, Liechtenstein, and Norway) or Switzerland",
        "id": 1,
        "question": "Why is my account associated with a region?"
    },
    {
        "answer": "Your account is associated with a region (or territory) in the Terms of Service so that we can determine several things:\r\n\r\nThe Google affiliate that provides the services, that processes your information, and that is responsible for complying with applicable privacy laws. Generally, Google offers its consumer services through either of two companies:\r\nGoogle Ireland Limited, if you’re located in the European Economic Area (EU countries plus Iceland, Liechtenstein, and Norway) or Switzerland",
        "id": 2,
        "question": "Why is my account associated with a region?"
    }
]

```

### POST api/faqs: Add FAQ.
#### URL
```json
http://localhost:5000/api/faqs/
```
#### Response:
```json
{
    "question":"what are parameters?",
    "answer":"lang is the parameter"
}
```
#### Response:

```json
{
    "message": "FAQ added successfully"
}
```
