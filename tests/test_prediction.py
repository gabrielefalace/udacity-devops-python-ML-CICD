from urllib import response
from app import app
from unittest import TestCase

class TestIntegration(TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_home(self):
        response = self.app.get("/")
        assert response.status_code == 200

    def test_prediction(self):
        response = self.app.post("/predict", 
            json={
                "CHAS":{"0":0},
                "RM":{"0":6.575},
                "TAX":{"0":296.0},
                "PTRATIO":{"0":15.3},
                "B":{"0":396.9},
                "LSTAT":{  "0":4.98}
                }, 
            headers={"Content-Type": "application/json"})

        print(">>> Status Code %s " % response.status_code)
        assert response.status_code == 200