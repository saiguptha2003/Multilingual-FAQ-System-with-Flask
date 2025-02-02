# Multilingual FAQ System with Flask

## This is a python based flask Application 
## flask is a python backend framework
--
####  Note: I made the .env file public to help avoid any difficulties when others clone the repository. It could be challenging for users to add their own .env file from another source, so I made it available. I have no issues with it being public, and I hope this makes the process easier for everyone.

#### For routes and details please visit http://localhost:5000/ for api details
--
## Assumptions:
#### Language Scalability via Translation API:

##### As the FAQ model may need to support a large number of languages, a translation API is used to automatically translate questions and answers. This helps manage vertical growth, allowing the system to scale and serve a larger, diverse language community without expanding the database structure.
#### Backend Framework - Flask:

##### The task allows flexibility in choosing backend technologies. Given the options of Node.js, Python (Django/Flask), and others, Flask was chosen as the backend server framework due to its simplicity, scalability, and ease of integration with other tools.

#### WYSIWYG Formatting - Summernote:
##### Instead of CKEditor, Summernote was selected for WYSIWYG (What You See Is What You Get) text formatting. Summernote was chosen because of its lightweight nature, ease of use, and compatibility with the application’s requirements, offering a similar functionality to CKEditor with a smaller footprint.
--

## Features
##### FAQ Management: Add FAQ entries.
##### Multilingual Support: Automatically translate FAQ questions and## answers into multiple languages.
##### SQLAlchemy Integration: Store FAQ data in a relational database using SQLAlchemy.
##### REST API: Expose APIs to fetch FAQ data and handle translations.
##### Redis Cache: It Helps to cache the frequently used keys over the values

--

## Technologies Used
### Flask: A lightweight WSGI web application framework for Python.
##### SQLAlchemy: ORM for database management.
##### Requests: For making HTTP requests to translation APIs.
##### JSON: Data exchange format for translating FAQ content.
##### Redis: Data caching server side
##### Docker : Container based development
--

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
--

## API Endpoints

#### GET api/faqs                               
###### Fetch all FAQs.
####  POST api/faqs                             
###### Create a new FAQ.
#### GET api/faqs?lang=bn                       
###### Fetch All FAQs in given language 
#### Template GET api/faqs/get_faqs_WYSIWYG     
###### Get the WYSIWYG text rendered with drop down of question and answer
#### Template POST FORM apifaqs/add_faq         
###### Form for adding faq
--

## Database Schema
#### The application uses SQLAlchemy for database interaction. The FAQ table schema is as follows:

##### id: Primary key (integer).
##### question: The FAQ question (string).
##### answer: The FAQ answer (text)

--

## Requests and Response

### GET api/faqs/?lang=te: Fetch all FAQs.
#### Description: This URL converts all FAQs into the specified language, removes all WYSIWYG formatting, and returns the FAQs in plain text format for better readability.
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
#### Discription : This endpoint retrieves all FAQs in English. If the questions and answers are in a different language, they are automatically translated into English. If they are already in English, no changes are made. The API response returns all FAQs with WYSIWYG-added HTML and formatting removed for better readability.
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
#### Request:
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


### GET api/faqs/add_faq : get FAQs without WYSIWYG formating.
#### URL
```json
http://localhost:5000/api/faqs/add_faq
```

#### View
![Alt text](/static/add_faq_with_WYSIWYG.png)

![Alt text](/static/add_faq.png)


### GET api/faqs/get_faqs_WYSIWYG : get FAQs without WYSIWYG formating.
#### URL
```json
http://localhost:5000/api/faqs/get_faqs_WYSIWYG
```

#### View
![Alt text](/static/get_faqs_with_WYSIWYG.png)

![Alt text](/static/get_faqs_WYSIWYG.png)

--

## Cache Imformation
### Implementation
1. create a cache key : faqs_<lang> ; lang can be any bi,hi,te,be,en
2. create a data count key : faqs_count_<lang> ; lang can be any bi,hi,te,be,en
3. get them from redis 
4. if count of faqs_count_<lang> is equal to db.count then returns the cached list of faqs 
5. if not then process the translations and returns the list and update the redis

--

## Testing 

```bash
cd app
pytest test.py
```

## Contact
### V D Panduranga Sai Guptha 
### 8688670712
### Saiguptha2003@gmail.com

