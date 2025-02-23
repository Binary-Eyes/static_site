from textnode import TextNode, TextType
from leafnode import LeafNode
from nodesplit import split_nodes_image, split_nodes_delimiter, split_nodes_link

def text_to_textnodes(text):
    if len(text) == 0:
        return []
    
    nodes = []
    source = TextNode(text, TextType.TEXT)
    bold_nodes = split_nodes_delimiter([source], "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter([source], "*", TextType.ITALIC)
    code_nodes = split_nodes_delimiter([source], "`", TextType.CODE)
    image_nodes = split_nodes_image([source])
    link_nodes = split_nodes_link([source])

    return nodes

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
