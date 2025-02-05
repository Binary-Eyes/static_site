import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_node_without_tag(self):
        node = ParentNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_node_with_empty_tag(self):
        node = ParentNode("", [])
        self.assertRaises(ValueError, node.to_html)

    def test_node_with_no_children(self):
        node = ParentNode("a", None)
        self.assertRaises(ValueError, node.to_html)

    def test_node_with_zero_children(self):
        node = ParentNode("h1", [])
        self.assertRaises(ValueError, node.to_html)

    def test_node_with_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode('b', "super book!")
            ])
        
        html = node.to_html()
        self.assertEqual(html, '<p><b>super book!</b></p>')
