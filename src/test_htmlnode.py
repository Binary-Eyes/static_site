import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_empty_props_to_html(self):
        node = HtmlNode()
        html_props = node.props_to_html()
        self.assertEqual(html_props, '')