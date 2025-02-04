from enum import Enum

class NodeType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode():
    def __Initi__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
