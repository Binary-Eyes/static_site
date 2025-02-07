import unittest

from textnode import TextNode, TextType
from conversions import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_converting_normal_node(self):
        text_node = TextNode("hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
