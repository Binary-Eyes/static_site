import unittest

from htmlnode import LeafNode

class TestLeafNodeToHtml(unittest.TestCase):
    def test_should_fail_when_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)


    def test_should_return_string_with_no_tag(self):
        node = LeafNode(None, "simple html text")
        html = node.to_html()
        self.assertEqual(html, "simple html text")


    def test_should_return_expected_for_simple_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = node.to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")


    def test_should_return_expected_for_tag_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = node.to_html()
        self.assertEqual(html, '<a href="https://www.google.com">Click me!</a>')

