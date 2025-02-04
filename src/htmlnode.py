class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        if len(self.props) == 0:
            return ""

        html = ''
        for entry in self.props:
            html += (f' {entry}="{self.props[entry]}"')

        return html
    
    def __repr__(self):
        return f'HtmlNode\nTag={self.tag}\nValue={self.value}\nChildren={self.children}\nProps={self.props}'
    