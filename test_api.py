import requests


BASE_URL = "http://localhost:5000/"

def test_WelcomeRoute():
    response = requests.get('http://localhost:5000/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")

def test_about():
    response = requests.get('http://localhost:5000/about')
    print(f"Status Code: {response.status_code}")
    data =response.json()
    print(data["name"])


def test_greet():
    response = requests.get('http://localhost:5000/greet/Rikki')
    print(f"Status Code: {response.status_code}")
    print(f"Name: {response.text}")
    assert "Hello, Rikki" in response.text

def test_calculate_add():
    response = requests.get('http://localhost:5000/calculate', params={"num1":1, "num2":2, "operation":"add"})
    print(f"Status Code: {response.status_code}")
    print(f"Calculate: {response.text}")
    assert "3" in response.text

def test_calculate_divide():
    response = requests.get('http://localhost:5000/calculate', params={"num1":4, "num2":0, "operation":"divide"})
    print(f"Status Code: {response.status_code}")
    #handle division by zero
    assert response.status_code == 500
    assert "An error occurred during calculation" in response.text

def test_echo():
    response = requests.post('http://localhost:5000/echo',json={"name": "Rikki Genack", "course":
        "MCON-357 - Backend Development", "semester":
                                                                     "Spring 2026"})
    print(f"Status Code: {response.status_code}")
    data = response.json()
    assert data["echoed"] is True

def test_status():
    response = requests.get('http://localhost:5000/calculate', params={"num1":4, "num2":0, "operation":"hello"})
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 400
    response = requests.post('http://localhost:5000/')
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 405

def test_custom_header():
    response = requests.get('http://localhost:5000/')
    custom_header = response.headers.get('X-Custom-Header')
    print(f"Custom Header: {custom_header}")

def test_err_handling():
    response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")





