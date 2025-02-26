import unittest

from parentnode import *
from leafnode import *

class TestParentNodeWithoutTag(unittest.TestCase):
    def test_should_fail(self):
        node = ParentNode(None, [], None);
        self.assertRaises(ValueError, node.to_html)

class TestParentNodeWithNoChildren(unittest.TestCase):
    def test_should_fail(self):
        node = ParentNode('a', None, None)
        self.assertRaises(ValueError, node.to_html)

class TestParentWithOneChild(unittest.TestCase):
    def test_should_return_expected_for_child_no_props(self):
        child_node = LeafNode('b', 'do not')
        node = ParentNode('a', [child_node])
        html = node.to_html()
        self.assertEqual(html, '<a><b>do not</b></a>')

class TestParentWithMultipleChildren(unittest.TestCase):
    def test_should_return_expected(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        html = node.to_html()
        self.assertEqual(html, '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

