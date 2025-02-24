import unittest
from textnode import *

class TestComparingTextNodes(unittest.TestCase):
    def test_should_return_true_for_same_node(self):
        node = TextNode("node", TextType.CODE, "www")
        self.assertEqual(node, node)

    def test_should_return_true_for_equal_nodes(self):
        node1 = TextNode("test node", TextType.NORMAL, "")
        node2 = TextNode("test node", TextType.NORMAL, "")
        self.assertEqual(node1, node2)

    def test_should_return_false_when_text_is_different(self):
        node1 = TextNode("test node 1", TextType.NORMAL, "")
        node2 = TextNode("test node 2", TextType.NORMAL, "")
        self.assertNotEqual(node1, node2)

    def test_should_return_False_when_type_is_different(self):
        node1 = TextNode("test node", TextType.BOLD, "")
        node2 = TextNode("test node", TextType.NORMAL, "")
        self.assertNotEqual(node1, node2)