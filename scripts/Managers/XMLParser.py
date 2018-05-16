from xml.etree.ElementTree import parse as _xmlParse

XMLNodes = []

class _XMLParser:
    def __init__(self, filePath):
        # Store the XML file path
        self._filePath = filePath
        # Boolean that store the validation boolean
        self.isValideFormat = False

        # Store the root of the XML datas
        self._root = _xmlParse(self._filePath).getroot()

        # Call validate function
        self._validate()

    """ Function called on the end of __init__ to validate input datas """
    def _validate(self):
        if self._root.tag == 'TextData':
            if self._root.attrib["version"] == "TD 1":
                self.isValideFormat = True

    """ Get the node given in argument (string) """
    def getNode(self, node):
        return self._root.find(node)


""" Store the nodes informations """
class NodeArray:
    def __init__(self, parent, node, sub=None):
        # Parent node data
        self._parent = parent
        # Current node data
        self._node = parent.getNode(node)
        # Array of subelements of the node
        self._array = self._node.findall(sub)

    """ Operator [] override (let us use the node["sub element"] form) """
    def __getitem__(self, item):
        for elem in self._array:
            if elem.get("type") == item:
                return elem.text
        return "-?-Unknown-?-"

    """ Getters """
    def GetParent(self):
        return self._parent

    def GetArray(self):
        return self._array

    def GetNode(self):
        return self._node


""" Init the XML datas with the given file (filepath) """
def InitXMLParser(filePath):
    # Create a instance of the _XMLParser
    XMLData = _XMLParser(filePath)

    # Check if the XMLParser if valid else raise a TypeError
    if XMLData.isValideFormat:
        return XMLData
    else:
        raise TypeError("XML Validation failed: unknown type")

"""
if __name__ == "__main__":
    # Exemple code 
    XMLData = InitXMLParser("..\\texts.xml")

    buttons = NodeArray(XMLData, "menu", "button")
    labels  = NodeArray(XMLData, "menu", "label")

    print(buttons["Camera"])
    print(labels["slides"])"""