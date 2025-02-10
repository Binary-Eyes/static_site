import unittest

from textnode import TextNode, TextType
from nodesplit import split_nodes_delimiter

class TestSplittingTextNodes(unittest.TestCase):
    def test_should_work(self):
        source_nodes = [
            TextNode("simple text node", TextType.TEXT),
            TextNode("with `code` and `code` life is good", TextType.TEXT),
            TextNode("some **bold**, some *italics*", TextType.TEXT)
        ]

        nodes = split_nodes_delimiter(source_nodes, "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 11)


class TestSplittingTextNodeWithIncompleteDelimiter(unittest.TestCase):
    def test_should_raise_exception(self):
        node = TextNode("this text is *invalid", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "*", TextType.ITALIC)


class TestSplittingTextNodeWithMultipleCodeBlocks(unittest.TestCase):
    def test_should_return_expected_node_count(self):
        node = TextNode("two code snippets `string cast` and `float cast` are working", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(split), 5)

    def test_should_return_expected_node_types(self):
        node = TextNode("two code snippets `string cast` and `float cast` are working", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)        
        self.assertEqual(split[0].node_type, TextType.TEXT)
        self.assertEqual(split[1].node_type, TextType.CODE)
        self.assertEqual(split[2].node_type, TextType.TEXT)
        self.assertEqual(split[3].node_type, TextType.CODE)
        self.assertEqual(split[4].node_type, TextType.TEXT)


class TestSplittingTextNodeWithOneCodeBlock(unittest.TestCase):
    def test_should_return_three_nodes(self):
        node = TextNode("the code snippet `float a = 1.0` sets a floating-point value", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(split), 3)

    def test_should_return_expected_node_types(self):
        node = TextNode("two code snippets `string cast` and `float cast` are working", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split[0].node_type, TextType.TEXT)
        self.assertEqual(split[1].node_type, TextType.CODE)
        self.assertEqual(split[2].node_type, TextType.TEXT)

    def test_should_return_expected_text_values(self):
        node = TextNode("the code snippet `float a = 1.0` sets a floating-point value", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split[0].text, "the code snippet ")
        self.assertEqual(split[1].text, "float a = 1.0")
        self.assertEqual(split[2].text, " sets a floating-point value")


class TestSplittingSimpleTextNode(unittest.TestCase):
    def test_should_return_expected_lenth(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(len(split), 1)
    
    def test_should_return_node_with_expected_text(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(split[0].text, "simple text")

    def test_should_return_node_with_text_type(self):
        node = TextNode("simple text", TextType.TEXT)
        split = split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(split[0].node_type, TextType.TEXT)