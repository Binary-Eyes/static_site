import unittest

from textnode import *
from markdown import split_nodes_link

class TestSplittingNodeWithLinks(unittest.TestCase):
    def test_should_return_expected_nodes(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        split = split_nodes_link([node])
        self.assertEqual(len(split), 4)