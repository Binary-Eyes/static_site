from textnode import TextNode, TextNodeType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    type = text_node.text_type
    if type == TextNodeType.NORMAL:
        return LeafNode(tag=None, value=text_node.text)
    if type == TextNodeType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    if type == TextNodeType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    pass
    