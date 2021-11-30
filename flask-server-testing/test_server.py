import time
from flask import Flask
from app import app

def test_base_route():
    client = app.test_client()
    url = '/average?integers=1&integers=5&integers=8'

    response = client.get(url)
    assert response.status_code == 200

def test_output():
    client = app.test_client()
    url = '/average?integers=1&integers=1'

    response = client.get(url)
    assert response.data == b'Average is : 1.0'

def test_stress():
    start_time = time.time()

    client = app.test_client()
    url = '/average?integers=1&integers=5&integers=8'
	
    for i in range(1000):
	    client.get(url)

    total_time = time.time()-start_time

    assert (total_time/1000) < 100