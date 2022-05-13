import unittest
from translator import english_to_french, french_to_english

class TestTranslators(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Goodbye'),'Au revoir')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def not_equal_test_english_to_french(self):
        self.assertNotEqual(english_to_french('Water'),'du Coca')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Au revoir'),'Goodbye')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def not_equal_test_french_to_english(self):
        self.assertNotEqual(french_to_english('du Coca'),'Water')

if __name__ == '__main__':
    unittest.main()