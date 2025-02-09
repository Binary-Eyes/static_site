import unittest

from textnode import TextNode, TextType
from conversions import split_nodes_delimiter

class TestSplittingTextNodeWithOneCodeBlock(unittest.TestCase):
    def test_should_return_three_nodes(self):
        node = TextNode("the code snippet 'float a = 1.0' sets a floating-point value")
        split = split_nodes_delimiter([node], "'", TextType.CODE)
        self.assertEqual(len(split), 3)
        pass

class TestSplittingSimpleTextNode(unittest.TestCase):
    def test_should_return_expected_lenth(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(len(split), 1)
        pass
    
    def test_should_return_node_with_expected_text(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(split[0].text, "simple text")
        pass

    def test_should_return_node_with_text_type(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(split[0].node_type, TextType.TEXT)
        pass