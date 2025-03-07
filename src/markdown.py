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

def split_nodes_image(source_nodes):
    nodes = []
    for source_node in source_nodes:
        if source_node.text == '':
            continue

        if source_node.text_type != TextType.TEXT:
            nodes.append(source_node)
            continue

        images = extract_markdown_images(source_node.text)
        if len(images) == 0:
            nodes.append(source_node)
            continue

        text = source_node.text
        for image in images:            
            image_tag = f"![{image[0]}]({image[1]})"
            split_text = text.split(image_tag, 1)
            if len(split_text) != 2:
                raise ValueError('invalid markdown: image section is incorrect')

            if split_text[0] != '':
                nodes.append(TextNode(split_text[0], TextType.TEXT))
            
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = split_text[1]
        
        if text != '':
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def split_nodes_link(source_nodes):
    nodes = []
    for source_node in source_nodes:
        if source_node.text == '':
            continue

        if source_node.text_type != TextType.TEXT:
            nodes.append(source_node)
            continue

        links = extract_markdown_links(source_node.text)
        if len(links) == 0:
            nodes.append(source_node)
            continue

        text = source_node.text
        for link in links:            
            link_tag = f"[{link[0]}]({link[1]})"
            split_text = text.split(link_tag, 1)
            if len(split_text) != 2:
                raise ValueError('invalid markdown: link section is incorrect')

            if split_text[0] != '':
                nodes.append(TextNode(split_text[0], TextType.TEXT))
            
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = split_text[1]
        
        if text != '':
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes