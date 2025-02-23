from textnode import TextNode, TextType
from extractions import extract_markdown_links, extract_markdown_images

def split_nodes_image(source_nodes):
    split_nodes = []    
    for source_node in source_nodes:
        images = extract_markdown_images(source_node.text)
        total_images = len(images)
        if total_images == 0:
            if len(source_node.text) > 0:
                split_nodes.append(source_node)
            continue

        image = images[0]
        image_text = f'![{image[0]}]({image[1]})'
        split_text = source_node.text.split(image_text, 1)
        if len(split_text) != 2:
            raise Exception("splitting text failed")

        if len(split_text[0]) > 0:            
            split_nodes.append(TextNode(split_text[0], TextType.TEXT))

        split_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        last = TextNode(split_text[1], TextType.TEXT)
        split_nodes.extend(split_nodes_image([last]))

    return split_nodes

def split_nodes_link(source_nodes):
    split_nodes = []    
    for source_node in source_nodes:
        links = extract_markdown_links(source_node.text)
        total_links = len(links)
        if total_links == 0:                
            if len(source_node.text) > 0:
                split_nodes.append(source_node)
            continue

        link = links[0]
        link_text = f'[{link[0]}]({link[1]})'
        split_text = source_node.text.split(link_text, 1)
        if len(split_text) != 2:
            raise Exception("splitting text failed")

        if len(split_text[0]) > 0:            
            split_nodes.append(TextNode(split_text[0], TextType.TEXT))

        split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        last = TextNode(split_text[1], TextType.TEXT)
        split_nodes.extend(split_nodes_link([last]))

    return split_nodes


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

        split_text = source_node.text.split(delimiter)
        if len(split_text)%2 == 0:
            raise ValueError(f"requested text for parsing has invalid delimiter count\nTEXT={source_node.text}\nDELIMITER={delimiter}")

        for i in range(0, len(split_text)):
            node = None
            if i%2 == 0:
                node = TextNode(split_text[i], TextType.TEXT)
            else:
                node = TextNode(split_text[i], text_type)
            
            target_nodes.append(node)

    return target_nodes