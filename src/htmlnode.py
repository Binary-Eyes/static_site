class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('child classes should supply this method')
    
    def props_to_html(self):
        html = ''
        if self.props is None or len(self.props) == 0:
            return html
        
        for entry in self.props:
            html += f' {entry}="{self.props[entry]}"'
        
        return html
    
    def __repr__(self):
        return f'HtmlNode({self.tag} {self.value} {self.children} {self.props})'
    

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
    

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError('parent node is missing a tag')
        
        if self.children is None or len(self.children) == 0:
            raise ValueError('parent node is missing children')
        
        props = self.props_to_html()
        html = f'<{self.tag}{props}>'
        for child in self.children:
            html += child.to_html()
            
        html += f'</{self.tag}>'
        return html