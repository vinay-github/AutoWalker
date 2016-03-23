
from libs import mylibs
from general_header_file import *
data_file="samplexml"


class main:
    def __init__(self):
        #Default variables
        self.browser_id="0"
        self.browser="0"
        self.ie_driver=IE_PATH
        self.selected_browser=IE

        #XML Points
        self.root="NULL"
        self.blocks={}
        self.no_blocks=0
        self.no_cases=0
        self.cases={}

        self.libs_obj = mylibs()

main_obj = main()
main_obj.libs_obj.getBrowser(main_obj)
main_obj.libs_obj.getRoot(main_obj,data_file)
main_obj.libs_obj.parseXMLRoot(main_obj)
main_obj.libs_obj.parseBlocks(main_obj.blocks[0],main_obj)
main_obj.libs_obj.parseBlocks(main_obj.blocks[1],main_obj)
#print(br)

