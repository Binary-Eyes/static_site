import unittest

from htmlnode import *

class TestHtmlNodeProps(unittest.TestCase):
    def test_empty_props_should_return_none(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), None)

    def test_single_property_returns_expected(self):
        node = HtmlNode(props={"href": "https://www.google.com"})
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com"')

    def test_two_properties_return_expected(self):
        node = HtmlNode(props={
            "href": "www.test.co.il",
            "target": "dev"})
        html = node.props_to_html()
        self.assertEqual(html, ' href="www.test.co.il" target="dev"')


class TestHtmlNodeToHtml(unittest.TestCase):
    def test_should_raise_exception(self):
        node = HtmlNode()
        self.assertRaises(NotImplementedError, node.to_html)