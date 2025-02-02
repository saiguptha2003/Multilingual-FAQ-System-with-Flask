import pytest
from unittest.mock import patch
from app import create_app
from .models import FAQ
from .cache import redisClient

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mock_redis():
    with patch.object(redisClient, 'get') as mock_get, patch.object(redisClient, 'set') as mock_set:
        yield mock_get, mock_set

def test_get_faqs(client, mock_redis):
    mock_get, mock_set = mock_redis
    mock_get.return_value = None
    mock_set.return_value = None

    response = client.get('/api/faqs')
    
    assert response.status_code == 200
    assert 'question' in response.json[0]
    assert 'answer' in response.json[0]

def test_get_faqs_with_cache(client, mock_redis):
    mock_get, mock_set = mock_redis
    mock_get.return_value = '[{"id":1,"question":"Why is my account associated with a region?","answer":"Some answer"}]'

    response = client.get('/api/faqs')
    
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]['question'] == "Why is my account associated with a region?"

def test_add_faq(client):
    data = {
        "question": "What is the purpose of a FAQ?",
        "answer": "To provide quick answers to common questions."
    }
    
    response = client.post('/api/faqs', json=data)
    
    assert response.status_code == 201
    assert response.json['message'] == "FAQ added successfully"
    
    faq = FAQ.query.filter_by(question="What is the purpose of a FAQ?").first()
    assert faq is not None

def test_cache_logic(client, mock_redis):
    mock_get, mock_set = mock_redis
    mock_get.return_value = None
    mock_set.return_value = None

    response = client.get('/api/faqs')
    assert mock_set.called

def test_translation(client):
    with patch('app.translation_api.translate') as mock_translate:
        mock_translate.return_value = "Translated Question"

        response = client.get('/api/faqs?lang=fr')

        assert response.status_code == 200
        assert "Translated Question" in response.json[0]['question']

if __name__ == '__main__':
    pytest.main()
