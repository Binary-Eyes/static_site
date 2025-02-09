from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    type = text_node.node_type
    if type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    if type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    if type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    if type == TextType.LINK:
        return LeafNode(tag='a', value=text_node.text, props={"href":f"{text_node.url}"})
    if type == TextType.IMAGE:
        return LeafNode(tag='img', value='', props={"src": f"{text_node.url}", "alt": f'{text_node.value}'})
    
    raise ValueError(f'unknown text-node type: {text_node.node_type}')

def split_nodes_delimiter(source_nodes, delimiter, text_type):
    target_nodes = []
    for source_node in source_nodes:
        if source_node.node_type != TextType.TEXT:
            target_nodes.append(source_node)
            continue

        text = source_node.text
        delimiter_count = text.count(delimiter)
        if delimiter_count == 0:
            target_nodes.append(source_node)
            continue

        split_nodes = source_node.text.split(delimiter)
        target_nodes.extend(split_nodes)

    return target_nodes
    