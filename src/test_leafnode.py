import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_node_with_no_value(self):
        node = LeafNode()
        self.assertRaises()
        