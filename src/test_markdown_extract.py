import unittest

from markdown import extract_markdown_images

class TestExtractImagesFromMarkdown(unittest.TestCase):
    def get_matches(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        return extract_markdown_images(text)

    def test_should_return_two_matches(self):
        self.assertEqual(len(self.get_matches()), 2)

    def test_should_return_expected_first_item(self):
        matches = self.get_matches()
        first = matches[0]
        self.assertEqual(first[0], "rick roll")

    def test_should_return_expected_second_item(self):
        matches = self.get_matches()
        second = matches[1]
        self.assertEqual(second[1], "https://i.imgur.com/fJRm4Vk.jpeg")
