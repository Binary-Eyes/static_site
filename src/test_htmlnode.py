import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_empty_props_to_html(self):
        node = HtmlNode()
        html_props = node.props_to_html()
        self.assertEqual(html_props, '')

    def test_one_props_to_html(self):
        node = HtmlNode(props={"target": "test_env"})
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' target="test_env"')