"""System module."""
import pytest
from webapp import myapp

@pytest.fixture
def app():
    app = myapp()

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
