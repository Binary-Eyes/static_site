import unittest

from leafnode import *

class TestLeafNodeToHtml(unittest.TestCase):
    def test_should_fail_when_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)