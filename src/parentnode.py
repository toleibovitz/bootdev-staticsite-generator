from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag.")
        if not self.children:
            raise ValueError("Not a parent node, no children.")
        html_str = ""
        #base case
        for child in self.children:
            child_str = child.to_html()
            html_str += child_str
        if self.props:
            props_str = self.props_to_html()
        else:
            props_str = ""
        html_str = f"<{self.tag}{props_str}>{html_str}</{self.tag}>"
        return html_str