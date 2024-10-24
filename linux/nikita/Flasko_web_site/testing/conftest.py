import pytest
from pymongo import MongoClient
from website import create_app

@pytest.fixture(scope="module")
def mongo_client():
    client = MongoClient("mongodb://localhost:27017")
    yield client
    client.close()
    
    
@pytest.fixture(scope="module")
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
        
@pytest.fixture(scope="module")
def test_dbname(mongo_client):
    dbname = mongo_client['user_auth']
    yield dbname
    mongo_client.drop_database("user_auth")
    
    
@pytest.fixture(scope="module")
def test_dbname2(mongo_client):
    dbname2 = mongo_client['user_note']
    yield dbname2
    mongo_client.drop_database("user_note")
   

@pytest.fixture
def math_func(x = 10, y = 5):
    return (x + y)

    
