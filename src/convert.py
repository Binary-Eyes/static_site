from textnode import *
from leafnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)

    raise Exception(f'unknown text type requested: {text_node.text_type}')