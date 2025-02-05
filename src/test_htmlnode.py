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

    def test_two_props_to_html(self):
        node = HtmlNode(props={"href":"www.test.com", "target":"prod"})
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="www.test.com" target="prod"')

    def test_tag_without_props_to_html(self):
        node = HtmlNode("a")
        start_tag = node.start_tag_to_html()
        end_tag = node.end_tag_to_html()
        self.assertEqual(start_tag, "<a>")
        self.assertEqual(end_tag, "</a>")

    def test_tag_with_props_to_html(self):
        node = HtmlNode("a", props={"href":"www.test.co.il"})
        start_tag = node.start_tag_to_html()
        end_tag = node.end_tag_to_html()
        self.assertEqual(start_tag, '<a href="www.test.co.il">')
        self.assertEqual(end_tag, "</a>")