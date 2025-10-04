from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        
        if self.props:
            props = self.props_to_html()
            # print(f"PROPS: {props}")
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
            
        