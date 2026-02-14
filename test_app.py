import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns 200 and correct message"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello! This is my DevOps CI/CD Demo" in response.data

def test_about_route(client):
    """Test the about route returns 200 and correct message"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"Flask, Docker, and GitHub Actions" in response.data
