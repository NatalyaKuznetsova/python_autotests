import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/10")
    assert response.status_code == 200 

def name_pet():
    response2 = requests.get("https://petstore.swagger.io/v2/pet/10")
    assert response2.json()['name'] == 'lolly'
