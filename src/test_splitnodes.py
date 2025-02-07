import unittest

from textnode import TextNode, TextNodeType
from conversions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_text(self):
        node = TextNode("this is a simple text node", TextNodeType.TEXT)
        split = split_nodes_delimiter([node], "`", TextNodeType.CODE)
        self.assertEqual(len(split), 1)
        self.assertEqual(split[0].text, "this is a simple text node")
        