import pytest

import sys
import os

# PYTHONPATH=. pytest --maxfail=1 --disable-warnings --tb=short


# Add the parent directory (root) to the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, home

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_two():
    assert 3==3

def test_one():
    assert True

def test_three():
    assert True

def test_four(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        "message": "Hello, Docker + Flask! ok",
        "success": True
    }

def test_home_function_direct():
    response, status_code = home()
    assert status_code == 200
    assert response['success']