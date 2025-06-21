import unittest
from scripts.preprocess import is_amharic

class TestIsAmharic(unittest.TestCase):
    def test_amharic_word(self):
        self.assertTrue(is_amharic('አማርኛ'))  # Amharic word

    def test_english_word(self):
        self.assertFalse(is_amharic('hello'))  # English word

    def test_mixed_word(self):
        self.assertTrue(is_amharic('አማርኛhello'))  # Mixed Amharic and English

    def test_empty_string(self):
        self.assertFalse(is_amharic(''))  # Empty string

    def test_numbers(self):
        self.assertFalse(is_amharic('12345'))  # Numbers only

    def test_special_characters(self):
        self.assertFalse(is_amharic('!@#$%'))  # Special characters only

    def test_amharic_character_in_middle(self):
        self.assertTrue(is_amharic('testአtest'))  # Amharic character in the middle

if __name__ == '__main__':
    unittest.main()