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
    def test_should_return_three_nodes(self):
        node = TextNode("image string ![image](www.image.png) is image", TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 3)

class TestSplittingNodeWithOneImageOnLeft(unittest.TestCase):
    def test_should_return_2_nodes(self):
        node = TextNode("![image](www.image.png) is image", TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 2)
    
    def test_should_return_expected_node_0(self):
        node = TextNode("![image](www.image.png) is image", TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(split[0].text, "image")
        self.assertEqual(split[0].text_type, TextType.IMAGE)
        self.assertEqual(split[0].url, "www.image.png")

class TestSplittingNodeWithOneImageOnRight(unittest.TestCase):
    def test_should_return_two_nodes(self):
        node = TextNode("image string ![image](www.image.png)", TextType.TEXT)
        split = split_nodes_image([node])
        self.assertEqual(len(split), 2)
