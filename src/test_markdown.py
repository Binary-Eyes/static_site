import unittest

from markdown import *
from textnode import *
from htmlnode import *

class TestTextNodeWithoutTags(unittest.TestCase):
    def test_should_return_expected(self):
        text = TextNode('just text', TextType.NORMAL)
        nodes = split_nodes_delimiter([text], '`', TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, 'just text')