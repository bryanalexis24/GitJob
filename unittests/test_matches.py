import unittest
from apis.resumeapi import is_valid_resume

class TestResumeValidation(unittest.TestCase):
    def test_empty_resume(self):
        self.assertFalse(is_valid_resume(""))
    def test_empty_resume(self):
        self.assertFalse(is_valid_resume(""))
    def test_short_resume(self):
        self.assertFalse(is_valid_resume("Python is the best"))
    def test_non_string_input(self):
        self.assertFalse(is_valid_resume("1237483718")) 
    def test_valid_resume(self):
        valid = "Experienced backend engineer with expertise in Python, AWS, and system design"
        self.assertTrue(is_valid_resume(valid))
    def test_whitespace_only(self):
        self.assertFalse(is_valid_resume("     "))
    def test_no_letters(self):
        slef.assertFalse(is_valid_resume(" 12345678 &%$@()*"))