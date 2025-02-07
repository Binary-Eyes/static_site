import unittest

from textnode import TextNode, TextNodeType

class TestTextNode(unittest.TestCase):
    def test_comparing_different_nodes(self):
        node1 = TextNode("test node", TextNodeType.TEXT)
        node2 = TextNode("another test node", TextNodeType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_comparing_similar_nodes(self):
        node1 = TextNode("test node", TextNodeType.TEXT)
        node2 = TextNode("test node", TextNodeType.TEXT)
        self.assertEqual(node1, node2)

    def test_comparing_same_node(self):
        node = TextNode("test text", TextNodeType.TEXT)
        self.assertEqual(node, node)
