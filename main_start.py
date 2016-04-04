
from libs import mylibs
from general_header_file import *
import unittest
data_file="samplexml"


class main:
    def __init__(self):
        #Default variables
        self.browser_id="0"
        self.browser="0"
        self.ie_driver=IE_PATH
        self.chrome_driver=CHROME_PATH
        self.selected_browser=CHROME

        #XML Points
        self.root="NULL"
        self.blocks={}
        self.no_blocks=0
        self.no_cases=0
        self.cases={}
        self.asserts={}
        self.case_units={}

        self.libs_obj = mylibs()


main_obj = main()
'''
main_obj.libs_obj.getBrowser(main_obj)
main_obj.libs_obj.getRoot(main_obj,data_file)
main_obj.libs_obj.parseXMLRoot(main_obj)

'''
class unittests(unittest.TestCase):
    def setUp(self):
        main_obj.libs_obj.getBrowser(main_obj)
        main_obj.libs_obj.getRoot(main_obj, data_file)
        main_obj.libs_obj.parseXMLRoot(main_obj)

    def test_sample(self):
        for i in range(main_obj.no_cases):
            case_units=main_obj.cases[i].text.split(DELIMITER)
            j=0
            for units in case_units:
                with self.subTest():
                    j=int(units)-1
                    #print(main_obj.blocks[j].attrib)
                    main_obj.libs_obj.parseBlocks(main_obj.blocks[j],main_obj)
                    self.assertIn(main_obj.asserts[j].text, main_obj.browser.title)

            #self.asserts_check(main_obj.asserts[j],main_obj)
            #print(main_obj.asserts[j].tag)


'''
class unittests(unittest.TestCase):
    def setUp(self):
        main_obj.libs_obj.getBrowser(main_obj)
        main_obj.libs_obj.getRoot(main_obj, data_file)
        main_obj.libs_obj.parseXMLRoot(main_obj)

    def test_sample(self):
        for i in range(main_obj.no_cases):
            case_units=main_obj.cases[i].text.split(DELIMITER)
            j=0
            for units in case_units:
                j=int(units)-1
                print(main_obj.blocks[j].attrib)
                main_obj.libs_obj.parseBlocks(main_obj.blocks[j],main_obj)
                #self.asserts_check(main_obj.asserts[j],main_obj)
                #print(main_obj.asserts[j].tag)


    def asserts_check(self, root, main_obj):
        self.root = root
        self.main_obj = main_obj
        assert_obj = unittests()
        for subchild in root:
            if subchild.tag == TITLE:
                assert_obj.assertIn(self.root.text, self.main_obj.browser.title)
        return
'''

        #print(main_obj.case_units)
        #main_obj.libs_obj.parseBlocks(main_obj.blocks[0],main_obj)
    #main_obj.libs_obj.parseBlocks(main_obj.blocks[1],main_obj)

#print(br)

