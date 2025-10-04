import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_simple_parent_with_leaf_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "More text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>More text</p>"
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode(None, "Paragraph inside div")]),
                ParentNode("ul", [
                    ParentNode("li", [LeafNode(None, "First item")]),
                    ParentNode("li", [LeafNode(None, "Second item")]),
                ]),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>Paragraph inside div</p><ul><li>First item</li><li>Second item</li></ul></div>"
        )

    def test_raises_error_without_tag(self):
        node = ParentNode(None, [LeafNode(None, "text")])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Missing tag.")

    def test_raises_error_without_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Not a parent node, no children.")

    def test_parent_with_props(self):
        # only if your HTMLNode supports props -> string like <div class="test">
        node = ParentNode(
            "div",
            [LeafNode(None, "Hello")],
            props={"class": "test", "id": "main"}
        )
        html = node.to_html()
        # Depending on implementation order of props dict, use assertIn instead of exact string
        self.assertTrue(html.startswith("<div"))
        self.assertIn('class="test"', html)
        self.assertIn('id="main"', html)
        self.assertIn(">Hello</div>", html)

if __name__ == "__main__":
    unittest.main()