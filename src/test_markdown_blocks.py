import unittest

from markdown import markdown_to_blocks, detemine_block_type, BlockType

class TestDeteminingBlockType(unittest.TestCase):
    def test_should_recognize_heading(self):
        type = detemine_block_type("## Heading!")
        self.assertEqual(type, BlockType.HEADING)

    def test_should_recognize_quote(self):
        type = detemine_block_type(">A\n>B")
        self.assertEqual(type, BlockType.QUOTE)

    def test_should_recognize_code(self):
        type = detemine_block_type("""```
public static class Program
{
    public static void Main(stirng[])
    {
        return 0;
    }                       
}
```""")
        self.assertEqual(type, BlockType.CODE)

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