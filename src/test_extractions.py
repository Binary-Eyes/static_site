import unittest

from extractions import extract_markdown_images, extract_markdown_links

class TestLinkExtraction(unittest.TestCase):
    def test_should_return_expected_count(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(len(matches), 2)

class TestImageExtraction(unittest.TestCase):
    def test_should_return_expected_count(self):        
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(len(matches), 2)

    def test_should_return_expected_first(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches[0], ("rick roll","https://i.imgur.com/aKaOqIh.gif"))

        