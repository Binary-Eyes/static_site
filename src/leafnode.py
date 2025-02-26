from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None or len(self.value) == 0:
            raise ValueError('leaf node must have a value')
        
        if self.tag is None or len(self.tag) == 0:
            return self.value
        
        props = self.props_to_html()
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'
        
    
