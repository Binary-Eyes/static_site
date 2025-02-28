import unittest

from textnode import *
from leafnode import *
from convert import *

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
        pass