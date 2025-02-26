import unittest

from leafnode import *

class TestLeafNodeToHtml(unittest.TestCase):
    def test_should_fail_when_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_should_return_string_with_no_tag(self):
        node = LeafNode(None, "simple html text")
        html = node.to_html()
        self.assertEqual(html, "simple html text")