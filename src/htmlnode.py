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
        
        return ""
        # for i in range(0, len(self.props)):
        #     entry = self.props[i]
        #     keyvalue = f"{entry}={self.props[entry]}"
        