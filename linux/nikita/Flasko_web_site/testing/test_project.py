from pymongo import MongoClient
import pytest


@pytest.mark.connection 
@pytest.mark.timeout(5)
def test_connection():
    client = MongoClient("mongodb://localhost:27017")
    assert client.admin.command("ping")["ok"] > 0
    
#First test should always run with '-x' option.   
@pytest.mark.connection 
def test_login(client):
    response = client.get("/login")
    assert response.status_code == 200


@pytest.mark.connection 
def test_home(client):
    response = client.get("/home")
    assert response.status_code == 200
    
    
@pytest.mark.connection 
def test_sign_up(client):
    response = client.get("/sign-up")
    assert response.status_code == 200
    

@pytest.mark.content    
def test_title(client):
    response = client.get("/home")
    assert b"<title>Home</title>" in response.data
    

@pytest.mark.content    
def test_textarea(client):
    response = client.get("/home")
    assert b'<textarea name="note_html" id="note_html" class="form-control"></textarea>' in response.data


@pytest.mark.content     
def test_h1(client):
    response = client.get("/home")
    assert b"<h1 align='center'>Your Notes</h1>" in response.data
    

@pytest.mark.content     
def test_label(client):
    response = client.get("/home")
    assert b'<label for="note">Notes</label>' in response.data
    

@pytest.mark.content   
def test_check_note_html(client):
    test_note = "aas"
    response = client.post('/home', data={'note_html': test_note}, follow_redirects=True)
    assert response.status_code == 200
    response = client.get('/home')
    assert "aas" in response.data.decode('utf-8')


@pytest.mark.db
def test_insert_user(test_dbname):
    collection = test_dbname["test_collection"]
    doc = {
        "first": "email"
    }
    result = collection.insert_one(doc)
    assert result.inserted_id is not None
    

@pytest.mark.db
def test_find_document(test_dbname):
    collection = test_dbname["test_collection"]
    doc = collection.find_one({"first": "email"})
    assert doc["first"] == "email"
    

@pytest.mark.test    
def test_math(math_func):
    assert math_func == 15
    

@pytest.mark.resgitration
def test_registration(client):
    test_mail = "test@test.com"
    test_name = "Tester"
    test_password = "test1234"
    
    response_post = client.post('/sign-up', data={'email': test_mail, 'first_name': test_name, 'password1': test_password, 'password2': test_password}, follow_redirects=True)
    assert response_post.status_code == 200
    assert "Account created!" in response_post.data.decode('utf-8')
    response_get = client.get('/sign-up')
    assert response_get.status_code == 200
    

@pytest.mark.login    
def test_login_user(client):
    response_post = client.post('/login', data={'email': 'test@test.com', 'password': 'test1234'})
    assert response_post.status_code == 302
    
    