import unittest

from textnode import TextNode, TextType
from conversions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_text(self):
        node = TextNode("this is a simple text node", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(split), 1)
        self.assertEqual(split[0].text, "this is a simple text node")
        
    def test_text_with_single_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)