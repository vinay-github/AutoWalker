import xml.etree.ElementTree as ET
from general_header_file import *

from selenium import webdriver


class mylibs :

    '''
        Function returns root of the xml file
        Inputs : path of XML file
        Returns : root of XML
    '''
    def getRoot(self,inputfile):
        tree = ET.parse(inputfile)
        self.root = tree.getroot()
        return(self.root)
    
    '''
        Function to initiate browser
        Inputs: browser name, driver path
        Returns: Success/Failure
    '''
    def getBrowser(self,driver_location,req_browser):
        if req_browser == IE:
            browz = webdriver.Ie(driver_location)
            self.browser= browz.get(INDEX)
        elif req_browser == CHROME:
            browz = webdriver.Chrome(driver_location)
            self.browser = browz.get(INDEX)
        return(self.browser)

    '''
    Reads XML and updates every units to namedtuple
    input: XML-root
    return: Success/Failure
    '''
    def readXML(self, root):
        print(root.tag,"=",root.attrib)
        print("*******************")
        for child in root:
            print(child.tag,"=",child.text)
        print("******************")

