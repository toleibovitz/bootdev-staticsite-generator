from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = HTMLNode("div","Hello, world!",None,{"class": "greeting", "href": "https://boot.dev"},)
    print(node)


if __name__ == "__main__":
    main()
