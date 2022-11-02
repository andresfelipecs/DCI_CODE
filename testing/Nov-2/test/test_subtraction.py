import unittest
from subtraction import sub

class TestSubtraction(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(sub(4, 2), 2)

if __name__ == '__main__':
    unittest.main()