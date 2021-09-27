from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}

        # test to check if Iris Virginica is classified correctly
def test_retrain():
    # defining a sample payload fo type list for the testcase
    payload: list= [{"sepal_length": 3,"sepal_width": 5,"petal_length": 3.3,"petal_width": 4.5,"flower_class": 'Iris Virginica'}]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        #print (payload)
        #print (response.json())
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful"}
