from textnode import TextType

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

    return new_nodes