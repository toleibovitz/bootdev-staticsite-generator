from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    node = LeafNode("p", "Hello, world!")
    node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    node2 = LeafNode(None, "Hello, world!")
    print(node.to_html())
    print(node1.to_html())
    print(node2.to_html())


if __name__ == "__main__":
    main()
