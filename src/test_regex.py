import unittest
import re

class TestSimpleRegex(unittest.TestCase):
    def test_should_return_expected_word(self):
        text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
        matches = re.findall(r"teapot", text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], 'teapot')