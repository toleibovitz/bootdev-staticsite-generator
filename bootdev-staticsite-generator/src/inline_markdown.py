import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise Exception("invalid markdown")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
               split_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass