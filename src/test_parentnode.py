import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_node_without_tag(self):
        node = ParentNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_node_with_empty_tag(self):
        node = ParentNode("", [])
        self.assertRaises(ValueError, node.to_html)
