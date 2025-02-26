from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError('parent node is missing a tag')
        
        if self.children is None or len(self.children) == 0:
            raise ValueError('parent node is missing children')
        
        