import unittest

def add(x, y):
    return x + y

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

if __name__ == '_main_':
    unittest.main()
