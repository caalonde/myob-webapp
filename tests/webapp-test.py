"""System module."""
import requests

def test_root():
    """A dummy docstring."""
    # Test 1 - Root url
    url = "http://localhost:5000/"
    response = requests.get(url)
    print(response.content)
    assert response.status_code == 200


def test_health():
    """A dummy docstring."""
    # Test 2 - Health endpoint
    url = "http://localhost:5000/health"
    response = requests.get(url)
    print(response.status_code)
    #if response.status_code == 200:
    #    print("Test 2 - Pass")
    assert response.status_code == 200


def test_metadata():
    """A dummy docstring."""
    # Test 2 - Test metadata
    url = "http://localhost:5000/metadata"
    response = requests.get(url)
    print(response.content)
    assert response.status_code == 200
