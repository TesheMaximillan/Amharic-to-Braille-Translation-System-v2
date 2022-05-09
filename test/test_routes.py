import unittest
import requests

class TestRoute(unittest.TestCase):
    def test_home(self):
        URL = "http://127.0.0.1:5000/"
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)

        URL = "http://127.0.0.1:5000/home"
        resp = requests.get(URL)
        self.assertEqual(resp.status_code, 200)



if __name__== "__main__":
    tester = TestRoute()

    tester.test_home