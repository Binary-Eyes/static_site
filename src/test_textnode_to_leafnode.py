import unittest

from textnode import *

class TestUnknownTextType(unittest.TestCase):
    def test_should_raise_exception(self):
        node = TextNode('', '')
        self.assertRaises(Exception, text_node_to_html_node, node)

class TestTextNodeConversion(unittest.TestCase):
    def test_should_return_html_no_tag(self):
        node = TextNode("it was the best of time", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
    
    def test_should_return_correct_html_text(self):
        node = TextNode("it was the best of time", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, 'it was the best of time')

class TestBoldTextConvert(unittest.TestCase):
    def test_should_return_expected_node(self):
        text_node = TextNode("bold!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'bold!')

class TestItalicTextConvert(unittest.TestCase):
    def test_should_return_expected_node(self):
        text_node = TextNode('your name', TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'your name')

class TestCodeTextConvert(unittest.TestCase):
    def test_should_return_expected_node(self):
        text_node = TextNode('printf("Hello, World!");', TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 'printf("Hello, World!");')

class TestLinkTextConvert(unittest.TestCase):
    def test_should_return_expected_node(self):
        text_node = TextNode("google", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "google")
        self.assertEqual(len(html_node.props), 1)
        self.assertEqual(html_node.props['href'], "www.google.com")

class TestImageTextConvert(unittest.TestCase):
    def test_should_return_expected_node(self):
        text_node = TextNode('cat', TextType.IMAGE, 'cat.png')
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(len(html_node.props), 2)
