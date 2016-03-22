
from libs import mylibs
data_file="samplexml"

class main:
    def __init__(self):
        browser_id="0"
        browz="0"

main_obj = main()
libs_obj = mylibs()

#root= libs_obj.getRoot(data_file)
#print(root)
#print(libs_obj.parseXMLRoot(root))

main_obj.browser_id,main_obj.browz=libs_obj.getBrowser("C:\Temp\src\IEDriverServer_x64\IEDriverServer", "Ie")

#print(br)

