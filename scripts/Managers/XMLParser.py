from xml.etree.ElementTree import parse as _xmlParse
from Models.Singloton import singleton
from os.path import dirname, join

XMLData = None

class XMLError(TypeError):
    def __init__(self, message):
        super(XMLError, self).__init__("XML Validation Error: " + message)

@singleton
class XMLParser:
    """
    constructor: XMLParser(filepath=None, sub_node=None, types_list=None)

    :raise TypeError: if first singloton instance dosn't contains the three arguments

    """

    def __init__(self, filepath, sub_node, types_list):
        """
        :param filepath: the path of the XML file
        :type filepath: string
        :param sub_node: the first sub node of the file (usually the language node
        :type sub_node: string
        :param types_list: list of all differents types of strigs contained in the XML
        :type types_list: list[string]
        """

        self.__unknownText = "-?-UNKNOWN-?-"

        self._root = _xmlParse(filepath).getroot()

        self._subNode = self._root.find(sub_node)
        self._nodesTypesList = types_list

        self._nodesArray = {}

        self._validate()
        self._populate()


    def _validate(self):
        """
        Validate the XML File (called automatically on constructor)

        Valide format is: <TextData version="TDv1">


        :raise XMLError: if the XML file don't match the exiged format

        """
        if self._root.tag != "TextData" or self._root.attrib["version"] != "TDv1":
            raise XMLError("Unknown file format (don't contain the right flags)")


    def _populate(self):
        """
        Populate the class datas with the XML datas

        """
        for node in self._nodesTypesList:
            self._nodesArray[node] = {data.get("type"):data.text for data in self._subNode.findall(node)}


    def __getElementByString(self, stringName):
        """
        Private method that return strign element by his address on the format "type@element"

        :param stringName: contain the address of the element
        :type stringName: str

        :return: string of the element on the XML or the self.__unknownText string

        """
        category,var = stringName.split('@')
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


def init_XMLParser(*args):
    """
    init_XMLParser(filepath=None, sub_node=None, types_list=None)


    note: the singloton instance is also saved on the XMLData global variable

    :param filepath: the path of the XML file
    :type filepath: string
    :param sub_node: the first sub node of the file (usually the language node)
    :type sub_node: string
    :param types_list: list of all differents types of strigs contained in the XML
    :type types_list: list[string]

    :return the singloton instance of XMLParser

    """
    global XMLData
    if XMLData is not None:
        print("Error: XMLParser is already initialized...")
    else:
        XMLData = XMLParser(*args)
        return XMLData

def path(file):
    """ Wrapper to prevent Sphinx and other script to change the working directory """
    _curdir = dirname(__file__)
    return join(_curdir + "\\..", file)