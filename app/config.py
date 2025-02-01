from dotenv import load_dotenv
import os

load_dotenv() 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'asdfasdfeweer32dewd2134131231313fdsvad')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///faq.db')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    AWS_ACCESS_KEY=os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY=os.getenv("AWS>SECERT_KEY")
    AWS_REGION=os.getenv("AWS_REGION")
    SERVICE=os.getenv("SERVICE")
    API_URL=os.getenv("API_URL")