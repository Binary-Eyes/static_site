import unittest

from textnode import TextNode, TextType
from nodesplit import split_nodes_link

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