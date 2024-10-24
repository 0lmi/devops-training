try:
    from main import app
    import unittest
    import mongomock

except Exception as e:
    print("Some Modules are Missing {}".format(e))
    
    
class TestApp(unittest.TestCase):
    def test_index_status(self):
        client = app.test_client(self)
        #response_1 = client.get("/home")
        response_2 = client.get("/sign-up")
        response_3 = client.get("/login")
        response_4 = client.get("/logout")
        
        #statuscode_1 = response_1.status_code
        statuscode_2 = response_2.status_code
        statuscode_3 = response_3.status_code
        statuscode_4 = response_4.status_code
        
        #self.assertEqual(statuscode_1, 200)
        self.assertEqual(statuscode_2, 200)
        self.assertEqual(statuscode_3, 200)
        self.assertEqual(statuscode_4, 302)
        
    def test_index_content(self):
        client = app.test_client(self)
        response = client.get("/login")
        
        self.assertTrue(b'<title>Login</title>' in response.data)
        self.assertTrue(b'<h3 align="center">Login</h3>' in response.data)
        self.assertTrue(b'<button type="submit" class="btn btn-primary">Login</button>' in response.data)
        self.assertTrue(b'<label for="password">Password</label>' in response.data)
        
        
            
class TestMongoDb(unittest.TestCase):
    def setUp(self):
        self.client = mongomock.MongoClient()
        self.db = self.client['test_database']
        self.collection = self.db['test_collection']
        self.data = ({"email": "test@mail.com", "first_name": "tester", "password1": "testpassword", "password2": "testpassword"})
        
    def test_insert_and_find(self):
        self.collection.insert_one(self.data)
        doc = self.collection.find_one({"email": "test@mail.com"})
        
        self.assertIsNotNone(doc)
        self.assertEqual(doc['email'], "test@mail.com")
        self.assertEqual(doc['password1'], "testpassword")
        self.assertEqual(doc['password2'], "testpassword")
    
        
if __name__ == "__main__":
    unittest.main()        
