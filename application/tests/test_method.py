from flask import Flask
import sys
sys.path.insert(1, '/home/mdmd/PYTHON/flask-app/')

from application.application import myapp

def method_test():
    test_app = myapp
    with test_app.test_client() as test_client:
        response = test_client.get('/tree')
    #assert response.get_data == "asghaaar"
    assert response.status_code == 200

