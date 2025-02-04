import unittest

from htmlnode import HtmlNode

class TestHtmlNodeProps(unittest.TestCase):
    def test_empty_props(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HtmlNode(props={"href": "https://binaryeyes.com"})
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://binaryeyes.com"')

    def test_two_props(self):
        node = HtmlNode(props={"href": "https://linking.ce", "target": "monkeys"})
        props = node.props_to_html()
        self.assertEqual(props, f' href="https://linking.ce" target="monkeys"')
