import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_image

class TestSplittingEmptyImageNode(unittest.TestCase):
    def test_should_return_expected(self):
        node = TextNode('', TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 0)
