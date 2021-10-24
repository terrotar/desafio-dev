import pytest
import requests


# Blueprint Home
# Get
def test_get_homepage():
    response = requests.get('http://127.0.0.1:5000')
    assert response.status_code == 200


# Blueprint Register
# Get
def test_get_register():
    response = requests.get('http://127.0.0.1:5000/cadastrar')
    assert 'Digite seu nome' in response.text


# Post with registered account(check first if already exists)
def test_post_user_already_exists_register():
    data = {"email": 'teste@gmail.com',
            "pwd": 'senha',
            "fname": 'Teste',
            "lname": '01'}
    response = requests.post("http://127.0.0.1:5000/cadastrar",
                             data=data)
    assert 'E-mail já cadastrado no sistema =s' in response.text


# Blueprint Login

# Success login
def test_post_success_login():
    data = {"email": 'teste@gmail.com',
            "pwd": 'senha'}
    response = requests.post("http://127.0.0.1:5000/login",
                             data=data)
    assert response.status_code == 200


# Success logout
def test_get_success_logout():
    response = requests.get("http://127.0.0.1:5000/logout")
    assert response.status_code == 200


# Invalid email
def test_post_invalid_email_login():
    data = {"email": 'teste123@gmail.com',
            "pwd": 'senha'}
    response = requests.post("http://127.0.0.1:5000/login",
                             data=data)
    assert response.status_code == 200


# Invalid password
def test_post_invalid_password_login():
    data = {"email": 'teste123@gmail.com',
            "pwd": 'senha123'}
    response = requests.post("http://127.0.0.1:5000/login",
                             data=data)
    assert 'E-mail e/ou senha está incorreta =x' in response.text
