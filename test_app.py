import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertIsNone(hello_world())  # Check if the function runs without error

if __name__ == '__main__':
    unittest.main()
