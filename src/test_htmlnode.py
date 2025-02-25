import unittest

from htmlnode import *

class TestHtmlNodeProps(unittest.TestCase):
    def test_empty_props_should_return_none(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), None)


class TestHtmlNodeToHtml(unittest.TestCase):
    def test_should_raise_exception(self):
        node = HtmlNode()
        self.assertRaises(NotImplementedError, node.to_html)