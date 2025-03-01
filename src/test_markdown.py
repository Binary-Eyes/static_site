import unittest

from markdown import *
from textnode import *
from htmlnode import *

class TestTextNodeWithCode(unittest.TestCase):
    def setup(self):
        text = TextNode("this code `print` will print", TextType.TEXT)
        return split_nodes_delimiter([text], "`", TextType.CODE)

    def test_should_return_3_nodes(self):
        nodes = self.setup();
        self.assertEqual(len(nodes), 3)
        

class TestTextWithBrokenCode(unittest.TestCase):
    def test_should_raise_exception(self):
        node = TextNode("word `code`, wrong `code", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, node, "`", TextType.CODE)