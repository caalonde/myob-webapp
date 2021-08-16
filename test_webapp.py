"""System module."""
from webapp import myapp

app = myapp()
client = app.test_client()

def test_root():
    url = "http://localhost:5000/"
    response = client.get(url)
    print(response.data)
    assert response.data == b'Hello World!'

def test_health():
    """A dummy docstring."""
    # Test 2 - Health endpoint
    url = "http://localhost:5000/health"
    response = client.get(url)
    assert response.status_code == 200

def test_metadata():
    """A dummy docstring."""
    # Test 2 - Test metadata
    url = "http://localhost:5000/metadata"
    response = client.get(url)
    assert response.status_code == 200
