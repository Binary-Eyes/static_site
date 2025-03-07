import unittest

from markdown import markdown_to_blocks

class TestSplittingEmptyText(unittest.TestCase):
    def test_should_return_empty_list(self):
        blocks = markdown_to_blocks('')
        self.assertEqual(len(blocks), 0)

class TestSplittingSimpleBlocks(unittest.TestCase):
    def test_should_return_expected(self):
        markdown = """
first block of **markdown**

second _block_ of markdown
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "first block of **markdown**")

class TestSplittingThreeBlocks(unittest.TestCase):
    def test_should_return_expected(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )