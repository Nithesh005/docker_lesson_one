import pytest

import sys
import os

# PYTHONPATH=. pytest --maxfail=1 --disable-warnings --tb=short


# Add the parent directory (root) to the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# def test_onw():
#     assert False

def test_two():
    assert True
    assert 3==3