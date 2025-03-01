import unittest

from markdown import *
from textnode import *
from htmlnode import *

class TestTextNodeWithBoldText(unittest.TestCase):
    def setup(self):
        text = TextNode("my is **amir**", TextType.TEXT)
        return split_nodes_delimiter([text], "**", TextType.BOLD)
    
    def test_should_return_2_nodes(self):
        self.assertEqual(len(self.setup()), 2)

class TestTextNodeWithMultipleCodeTags(unittest.TestCase):
    def setup(self):
        text = TextNode("this is `code1` and this is `code2`", TextType.TEXT)
        return split_nodes_delimiter([text], "`", TextType.CODE)
    
    def test_should_return_4_nodes(self):
        self.assertEqual(len(self.setup()), 4)

class TestTextNodeWithCode(unittest.TestCase):
    def setup(self):
        text = TextNode("this code `print` will print", TextType.TEXT)
        return split_nodes_delimiter([text], "`", TextType.CODE)

    def test_should_return_3_nodes(self):
        nodes = self.setup();
        self.assertEqual(len(nodes), 3)

    def test_should_return_node_0_text(self):
        self.assertEqual(self.setup()[0].text_type, TextType.TEXT)

    def test_should_return_node_1_code(self):
        self.assertEqual(self.setup()[1].text_type, TextType.CODE)

    def test_should_return_node_2_text(self):
        self.assertEqual(self.setup()[2].text_type, TextType.TEXT)
        

class TestTextWithBrokenCode(unittest.TestCase):
    def test_should_raise_exception(self):
        node = TextNode("word `code`, wrong `code", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, node, "`", TextType.CODE)