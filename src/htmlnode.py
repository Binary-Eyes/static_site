class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('child classes should supply this method')
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return None
        
        html = ''
        for entry in self.props:
            html += f' {entry}="{self.props[entry]}"'
        
        return html