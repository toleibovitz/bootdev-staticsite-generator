import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

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
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        org_text = node.text
        images = extract_markdown_images(org_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = org_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            org_text = sections[1]
        if org_text != "":
            new_nodes.append(TextNode(org_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        org_text = node.text
        links = extract_markdown_links(org_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = org_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            org_text = sections[1]
        if org_text != "":
            new_nodes.append(TextNode(org_text, TextType.TEXT))
    return new_nodes

        