import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_image

class TestSplittingEmptyImageNode(unittest.TestCase):
    def test_should_return_expected(self):
        node = TextNode('', TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 0)


class TestSplittingNodeWithNoImage(unittest.TestCase):
    def test_should_return_expected(self):
        node = TextNode('there are no images in here', TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 1)
        self.assertEqual(split[0].text, 'there are no images in here')


class TestSplittingNodeWithOneImageInMiddle(unittest.TestCase):
    def get_nodes(self):
        node = TextNode("image string ![image](www.image.png) is image", TextType.TEXT)
        return [node]
    
    def test_should_return_three_nodes(self):
        split = split_nodes_image(self.get_nodes())
        self.assertEqual(len(split), 3)
