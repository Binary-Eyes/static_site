import unittest

from textnode import *
from markdown import *

class TestSimpleTextSplitting(unittest.TestCase):
    def test_should_return_expected(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)