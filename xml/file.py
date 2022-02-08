from asyncio import Handle
from email import parser
from logging import Handler
import xml.sax

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.model = ""
        self.speed = ""
    
    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "car":
            print("--CAR--")
            name = attributes["name"]
            print("name: ", name)
    
    def endElement(self, tag):
        if self.currentData == "model":
            print("model: ", self.model)
        elif self.currentData == "speed":
            print("speed: ", self.speed)
        self.currentData = ""
    
    def characters(self, content):
        if self.currentData == "model":
            self.model = content
        elif self.currentData == "speed":
            self.speed = content

if (__name__ == "__main__" ):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = XMLHandler()
    parser.setContentHandler(Handler)

    parser.parse("example.xml") 