import unittest

from textnode import TextNode, TextType
from nodesplit import split_nodes_link

class TestSplittingNodeNoLinks(unittest.TestCase):
    def test_should_return_one_node(self):
        node = TextNode("this is a node without a link", TextType.TEXT)
        split = split_nodes_link([node])
        self.assertEqual(len(split), 1)
        pass

    def test_should_return_expected_text_node(self):
        pass