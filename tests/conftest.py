import pytest
from webapp import myapp

@pytest.fixture
def app():
    app = myapp()

@pytest.fixture
def client(app):
    return app.test_client()
