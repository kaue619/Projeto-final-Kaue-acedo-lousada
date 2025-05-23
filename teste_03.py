import requests

def test_login_reqres():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/login", json=payload)
    data = response.json()
    assert "token" in data, "Token não encontrado na resposta"
