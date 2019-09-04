import server
import unittest
from model import connect_to_db




class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes"""

    def test_index(self):
        """make sure index page returns currect HTML"""

        #create test client
        client = server.app.test_client()

        # Use the test client to make requests
        result = client.post('/processlogin', data={'username':'Frodo','password':'ring'}, follow_redirects=True)

        # Compare result.data with assert method
        self.assertIn(b'<p>Drop image here</p>', result.data)


if __name__ == '__main__':
    # If called like a script, run our tests
    connect_to_db(server.app, )
    # server.app.run(host="0.0.0.0")
    unittest.main()