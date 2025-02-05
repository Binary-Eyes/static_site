from textnode import TextNode, TextNodeType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    type = text_node.text_type
    if type == Text