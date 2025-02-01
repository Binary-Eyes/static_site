import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_equal_text(self):
        node1 = TextNode("A", TextType.BOLD)
        node2 = TextNode("B", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_equal_type(self):
        node1 = TextNode("A", TextType.BOLD)
        node2 = TextNode("A", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

