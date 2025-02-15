import unittest

from textnode import TextNode, TextType
from nodesplit import split_nodes_link, split_nodes_image

class TestSplittingNodeWithImage(unittest.TestCase):
    def test_should_return_expected(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 2)


class TestSplittingNodeWithMultipleLinks(unittest.TestCase):
    def test_should_return_expected(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 4)


class TestSplittingNodeWithOneLink(unittest.TestCase):
    def test_should_return_expected_node_count(self):
        node = TextNode("click on [awesome link](www.google.com) to go to google", TextType.TEXT)
        split = split_nodes_link([node])
        self.assertEqual(len(split), 3)
        

class TestSplittingNodeNoLinks(unittest.TestCase):
    def test_should_return_one_node(self):
        node = TextNode("this is a node without a link", TextType.TEXT)
        split = split_nodes_link([node])
        self.assertEqual(len(split), 1)

    def test_should_return_expected_text_node(self):
        node = TextNode("this is a node without a link", TextType.TEXT)
        split = split_nodes_link([node])
        self.assertEqual(split[0].text, "this is a node without a link")