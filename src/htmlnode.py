

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [children]
        self.props = props

    def __repr__(self):
        pass

    def to_html(self):
        raise NotImplementedError("Child class should implement this")
    
    def props_to_html(self):
        if not self.props:
            raise ValueError("No properties for this node")
        
        props_str = ""
        for k, v in self.props.items():
            props_str += f' {k}="{v}"'

        return props_str