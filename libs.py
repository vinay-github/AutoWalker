from selenium import webdriver
from general_header_file import *
from lxml import etree
from io import StringIO

class mylibs:

    '''
        Function to initiate browser
        Inputs: browser name, driver path
        Returns: Success/Failure
    '''
    def getBrowser(self,driver_location,req_browser):
        if req_browser == IE:
            self.browz = webdriver.Ie(driver_location)
            self.browser= self.browz.get(INDEX)
        elif req_browser == CHROME:
            browz = webdriver.Chrome(driver_location)
            self.browser = self.browz.get(INDEX)
        return(self.browser,self.browz)

    '''
        Function returns root of the xml file
        Inputs : path of XML file
        Returns : root of XML
    '''
    def getRoot(self,inputfile):

        self.root = etree.parse(inputfile).getroot()
        return(self.root)


    '''
        Function parses all the children and subchildren of root
        Inputs : XML Root
        Returns : Success/Failure
    '''
    def parseXMLRoot(self,root):
        blocks={}
        print(root.text)
        print("************#**")
        tmp=0
        for child in root:
            if len(child):
                if child.tag == CONTENT:
                    for subchild in child:
                        blocks[tmp]=subchild
                        tmp=tmp+1
                        #print(subchild.get("n" and "desc") if subchild.attrib else subchild.text)
                        print("**********************")


        return(root)
'''
    def url_access(self,root):
        #Perform url accessing function


    def click_submit(self,root):
        #Perform click or submit function

    def text_entry(self,root):
        #Perform text entry

    def password_entry(self,root):
        #Perform password entry function

    def dropdown_selection(self,root):
        #Select dropdown

    def true_checking(self,root):
        #Check true part for validation

    def default_tag(self,root):
        #Perform action when tag doesn't match your requirement

    def parseBlocks(self,root):
        self.localroot = root
        for subroot in self.localroot:
            if subroot.tag == URL:
                #call url accessing function
                url_access(subroot)
            elif subroot.tag == CLICK:
                #call click function
                click_submit(subroot)
            elif subroot.tag == TEXT:
                # call text entering function
                text_entry(subroot)
            elif subroot.tag == PASSWORD:
                #call password entering function
                password_entry(subroot)
            elif subroot.tag == DROPDOWN:
                #call dropdown selecting function
                dropdown_selection(subroot)
            elif subroot.tag == TRUE:
                true_checking(subroot)
                #call validation function to validate
            else
                #call default function which says that xml tag is unknown
                default_tag(subroot)
'''
