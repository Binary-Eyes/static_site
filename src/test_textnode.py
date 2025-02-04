import unittest

from textnode import TextNode, NodeType

class TestTextNode(unittest.TestCase):
    def test_comparing_different_nodes(self):
        node1 = TextNode("test node", NodeType.NORMAL)
        node2 = TextNode("another test node", NodeType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_comparing_similar_nodes(self):
        node1 = TextNode("test node", NodeType.NORMAL)
        node2 = TextNode("test node", NodeType.NORMAL)
        self.assertEqual(node1, node2)

    def test_comparing_same_node(self):
        node = TextNode("test text", NodeType.NORMAL)
        self.assertEqual(node, node)
