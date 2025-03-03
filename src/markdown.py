import re
from textnode import *

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if len(old_nodes) == 0:
        return None
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split = old_node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception(f'at least one delimiter in text is not closed: {old_node.text} [{delimiter}]')
        
        for i in range(0, len(split)):
            if len(split[i]) == 0:
                continue

            node_type = TextType.TEXT
            if i%2 != 0:
                node_type = text_type
            new_nodes.append(TextNode(split[i], node_type))

    return new_nodes