from textnode import TextNode, TextNodeType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    type = text_node.node_type
    if type == TextNodeType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if type == TextNodeType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    if type == TextNodeType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    if type == TextNodeType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    if type == TextNodeType.LINK:
        return LeafNode(tag='a', value=text_node.text, props={"href":f"{text_node.url}"})
    if type == TextNodeType.IMAGE:
        return LeafNode(tag='img', value='', props={"src": f"{text_node.url}", "alt": f'{text_node.value}'})
    
    raise ValueError(f'unknown text-node type: {text_node.node_type}')

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for source_node in old_nodes:
        if source_node.node_type == TextNodeType.TEXT:
            split_nodes.append(source_node)

    return split_nodes
    