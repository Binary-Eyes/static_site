import unittest

from textnode import TextNode, TextNodeType
from conversions import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_converting_normal_node(self):
        text_node = TextNode("hello", TextNodeType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
