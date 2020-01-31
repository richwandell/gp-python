import unittest
from unittest import TestLoader, TextTestRunner, TestSuite
from flask import Response
from app import app


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client

    def test_multiply(self):
        res: Response = self.client.get("/multiply/5/5")
        self.assertEqual(25, int(res.get_data()))

    def test_display(self):
        res: Response = self.client.get('/display')
        self.assertEqual(res.get_data().decode().strip(), "Lorem Ipsum")

    def test_display_some_text(self):
        input = "some text"
        res: Response = self.client.get('/display/%s' % input)
        self.assertEqual(res.get_data().decode().strip(), input)


if __name__ == "__main__":
    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in (TestCase, )
    ]
    suite = TestSuite(tests)
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
