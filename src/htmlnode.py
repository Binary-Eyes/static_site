class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError('method should be implemented by child classes')
    

    def end_tag_to_html(self):
        if self.tag is None or self.tag == '':
            return ''

        return f'</{self.tag}>'
    

    def start_tag_to_html(self):
        if self.tag is None or self.tag == '':
            return ''
        return f'<{self.tag}{self.props_to_html()}>'
        

    def props_to_html(self):
        if self.props is None:
            return ''
        
        html = ''
        for entry in self.props:
            html += f' {entry}="{self.props[entry]}"'
        
        return html
    
    def __repr__(self):
        text = f'{self.tag}, {self.value}, {self.props_to_html}'
        if self.children is not None:
            for child in self.children:
                text += f'\tchild: {child}\n'
        