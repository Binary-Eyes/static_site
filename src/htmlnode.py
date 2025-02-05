class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('method should be implemented by child classes')
    
    def props_to_html(self):
        if self.props == None:
            return ''
        
        html = ''
        for entry in self.props:
            html += f' {entry}="{self.props[entry]}"'
        
        return html