import unittest

from textnode import TextNode, TextType
from conversions import text_node_to_html_node, text_to_textnodes

class TestTextConversion(unittest.TestCase):
    def test_should_return_expected_count(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)

class TestEmptyTextToNodes(unittest.TestCase):
    def test_should_return_zero_nodes(self):
        nodes = text_to_textnodes('')
        self.assertEqual(len(nodes), 0)

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_converting_normal_node(self):
        text_node = TextNode("hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
