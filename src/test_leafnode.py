import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag(self):
        node = LeafNode('p', "this is a test paragraph!")
        html = node.to_html()
        self.assertEqual(html, '<p>this is a test paragraph!</p>')

    def test_leaf_node_without_tag(self):
        node = LeafNode(None, "raw text dog")
        html = node.to_html()
        self.assertEqual(html, "raw text dog")

    def test_leaf_node_will_all(self):
        node = LeafNode('a', 'click me!', {"href": "www.clickme.com"})
        html = node.to_html()
        self.assertEqual(html, '<a href="www.clickme.com">click me!</a>')
        