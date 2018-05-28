from xml.etree.ElementTree import parse as _xmlParse
from BPL import Singloton

XMLData = None

class XMLError(Exception):
    def __init__(self, message):
        super(XMLError, self).__init__("XML Validation Error: " + message)

class XMLParser(Singloton):
    """constructor: XMLParser(filepath=None, sub_node=None, types_list=None)

    :param args: filepath, sub_node, types_list
    :arg filepath: the path of the XML file
    :type filepath: str
    :arg sub_node: the first sub node of the file (usually the language node
    :type sub_node: str
    :arg types_list: list of all differents types of strigs contained in the XML
    :type types_list: list[str]

    :raise TypeError: if first singloton instance dosn't contains the three arguments
    """

    class __XMLParser(object):
        def __init__(self, filepath, sub_node, types_list):

            self.__unknownText = "-?-UNKNOWN-?-"

            self._root = _xmlParse(filepath).getroot()

            self._subNode = self._root.find(sub_node)
            self._nodesTypesList = types_list

            self._nodesArray = {}
            # self._indexRegistery = []

            self._validate()
            self._populate()

        def _validate(self):
            """
            Validate the XML File (called automatically on constructor)

            :raise TypeError if the XML file don't match the exiged format
            """
            if self._root.tag != "TextData" or self._root.attrib["version"] != "TDv1":
                raise XMLError("Unknown file format (don't contain the right flags)")

        def _populate(self):
            """
            Populate the class datas with the XML datas
            """
            for node in self._nodesTypesList:
                self._nodesArray[node] = {data.get("type"):data.text for data in self._subNode.findall(node)}
                # self._indexRegistery.append(node)

        """
        ### deprecated ###
        def __getElementByID(self, item):
            if len(self._indexRegistery) > item:
                return self._nodesArray[self._indexRegistery[item]]
            return self.__unknownText
        """

        def __getElementByString(self, string):
            """
            Private method that return strign element by his address (format: type@element)
            :param string: contain the address of the element (format: "type@element")
            :type string: str
            :return: string of the element on the XML or the self.__unknownText string
            """
            category,var = string.split('@')
            if category in self._nodesArray:
                if var in self._nodesArray[category]:
                    return self._nodesArray[category][var]
            return self.__unknownText


        def __getitem__(self, item):
            if type(item) is str:
                if '@' in item:
                    return self.__getElementByString(item)
                else:
                    if item in self._nodesArray:
                        return self._nodesArray[item]

            return self.__unknownText

    def __getitem__(self, item):
        return self.instance[item]

    _ClassName = __XMLParser

def init_XMLParser(*args):
    """init_XMLParser(filepath=None, sub_node=None, types_list=None)

    :param args: filepath, sub_node, types_list

    :arg filepath: the path of the XML file
    :type filepath: str
    :arg sub_node: the first sub node of the file (usually the language node
    :type sub_node: str
    :arg types_list: list of all differents types of strigs contained in the XML
    :type types_list: list[str]
    :return XMLParser

    note: the singloton instance is also saved on the XMLData global variable
    """
    global XMLData
    if XMLData is not None:
        print("Error: XMLParser is already initialized...")
    else:
        XMLData = XMLParser(*args)
        return XMLData