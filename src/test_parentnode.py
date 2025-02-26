import unittest

from parentnode import *

class TestParentNodeWithoutTag(unittest.TestCase):
    def test_should_fail(self):
        node = ParentNode(None, [], None);
        self.assertRaises(ValueError, node.to_html)

class TestParentNodeWithNoChildren(unittest.TestCase):
    def test_should_fail(self):
        node = ParentNode('a', None, None)
        self.assertRaises(ValueError, node.to_html)
