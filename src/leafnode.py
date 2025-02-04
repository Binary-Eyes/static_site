from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('leaf node must have value')
        
        if self.tag == None:
            return self.value
        
        return f'{self.__get_starg_tag()}{self.value}</{self.tag}>'
    
    def __get_starg_tag(self):
        if len(self.props) == 0:
            return f'<{self.tag}>'
        else:
            return f'<{self.tag} {self.props_to_html()}>'
