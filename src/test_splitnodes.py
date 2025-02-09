import unittest

from textnode import TextNode, TextType
from conversions import split_nodes_delimiter

class TestSplittingSimpleTextNode(unittest.TestCase):
    def test_should_return_expected_lenth(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(len(split), 1)
        pass
    
    # def test_should_return_node_with_expected_text(self):
    #     node = TextNode("simple text", TextType.TEXT)
    #     split = split_nodes_delimiter(node, '*', TextType.ITALIC)
    #     self.assertEqual(split[0].text, "simple text")
    #     pass

    # def test_should_return_node_with_text_type(self):
    #     node = TextNode("simple text", TextType.TEXT)
    #     split = split_nodes_delimiter(node, '*', TextType.ITALIC)
    #     self.assertEqual(split[0].node_type, TextType.TEXT)
    #     pass