import server
import unittest
from model import connect_to_db, db
from model import example_data



class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes"""

    # def test_login(self):
    #     """make sure index page returns currect HTML"""

    #     #create test client
    #     client = server.app.test_client()

    #     # Use the test client to make requests
    #     result = client.post('/processlogin', data={'username':'Frodo','password':'ring'}, follow_redirects=True)

    #     # Compare result.data with assert method
    #     self.assertIn(b'<p>Drop image here</p>', result.data)

    def setUp(self):
        print('hello!!!')
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        
        connect_to_db(server.app, "testdb")

        db.create_all()
        example_data()


    def test_register(self):
        """make sure index page returns currect HTML"""

        #create test client
        client = server.app.test_client()

        # Use the test client to make requests
        result = client.post('/process_register', data={'username':'me', 'firstname':'Jessica','lastname':'Gamio','password':'abc'}, follow_redirects=True)

        # Compare result.data with assert method
        self.assertIn(b'<p>Drop image here</p>', result.data)


if __name__ == '__main__':
    # If called like a script, run our tests
    # connect_to_db(server.app)
    # connect_to_db(server.app, "testdb")
    print('hello')
    unittest.main()
