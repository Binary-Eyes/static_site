from textnode import TextNode, TextType

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
        for i in range(0, len(split_text)):
            node = None
            if i%2 == 0:
                node = TextNode(split_text[i], TextType.TEXT)
            else:
                node = TextNode(split_text[i], text_type)

            target_nodes.append(node)

    return target_nodes