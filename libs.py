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
    def getBrowser(self, main_obj):
        self.main_obj=main_obj
        if self.main_obj.selected_browser == IE:
            self.main_obj.browser=webdriver.Ie(self.main_obj.ie_driver)
            print(self.main_obj.browser.get(INDEX))

        elif self.main_obj.selected_browser == CHROME:
            webdriver.Chrome(self.main_obj.ie_driver).get(INDEX)

    '''
        Function returns root of the xml file
        Inputs : path of XML file
        Returns : root of XML
    '''
    def getRoot(self,main_obj,inputfile):
        self.main_obj=main_obj
        self.main_obj.root = etree.parse(inputfile).getroot()
       # return(self.root)


    '''
        Function parses all the children and subchildren of root
        Inputs : XML Root
        Returns : Success/Failure
    '''
    def parseXMLRoot(self,main_obj):
        self.main_obj = main_obj
        for child in self.main_obj.root:
            if len(child):
                if child.tag == CONTENT:
                    for subchild in child:
                        self.main_obj.blocks[self.main_obj.no_blocks]=subchild
                        self.main_obj.no_blocks+=1
                        print(subchild.get("n" and "desc") if subchild.attrib else subchild.text)
                elif child.tag == CASES:
                    for subchild in child:
                        self.main_obj.cases[self.main_obj.no_cases]=subchild
                        print(subchild.text)
                        self.main_obj.no_cases+=1

    def url_access(self,root,main_obj):
        """
        :rtype: object
        """
        self.root=root
        self.main_obj=main_obj
        if root.tag == URL and root.attrib :
            key=self.root.keys()
            url=self.root.get(key[0])
            self.main_obj.browser.get(url)

    def click_submit(self,root,main_obj):
        #Perform click or submit function
        self.root=root
        self.main_obj=main_obj
        key=self.root.keys()
        self.type=self.root.get(key[0])
        self.click=self.root.get(key[1])
        if self.type == ID:
            self.main_obj.browser.find_element_by_id(self.click).click()
        elif self.type == NAME:
            self.main_obj.browser.find_element_by_name(self.click).click()

    def text_entry(self,root, main_obj):
        self.root=root
        self.main_obj=main_obj
        key=self.root.keys()
        self.type=self.root.get(key[0])
        self.text=self.root.get(key[1])
        if self.type == ID:
            self.main_obj.browser.find_element_by_id(self.text).send_keys(self.root.text)
        elif self.type == NAME:
            self.main_obj.browser.find_element_by_name(self.text).send_keys(self.root.text)

    def password_entry(self,root, main_obj):
        self.root=root
        self.main_obj=main_obj
        key=self.root.keys()
        self.type=self.root.get(key[0])
        self.pwd=self.root.get(key[1])
        if self.type == ID:
            self.main_obj.browser.find_element_by_id(self.pwd).send_keys(self.root.text)
        elif self.type == NAME:
            self.main_obj.browser.find_element_by_name(self.pwd).send_keys(self.root.text)

    def parseBlocks(self,root,main_obj):
        self.localroot = root
        self.main_obj = main_obj
        for subroot in self.localroot:
            if subroot.tag == URL:
                self.url_access(subroot,self.main_obj)
            elif subroot.tag == CLICK:
                self.click_submit(subroot,self.main_obj)
            elif subroot.tag == TEXT:
                # call text entering function
                self.text_entry(subroot,self.main_obj)
            elif subroot.tag == PASSWORD:
                #call password entering function
                self.password_entry(subroot,self.main_obj)

'''


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

'''



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


'''
