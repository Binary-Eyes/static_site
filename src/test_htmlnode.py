import unittest

from htmlnode import HtmlNode

class TestHtmlNodeProps(unittest.TestCase):
    def test_empty_props(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

