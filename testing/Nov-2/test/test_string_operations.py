import unittest
from string_operations import titleize
from string_operations import join_names

class Test_String_Operations(unittest.TestCase):
    
    def test_titleize(self):
        self.assertEqual(titleize('felipe', 'castro'), ('Felipe', 'Castro'))

    def test_join_names(self):
        lst = ['felipe', 'castro', 'salazar']
        self.assertEqual(join_names(lst), 'felipe castro salazar')

if __name__ == '__main__':
    unittest.main()