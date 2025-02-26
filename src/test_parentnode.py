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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")
