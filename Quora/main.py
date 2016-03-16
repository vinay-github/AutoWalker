#Defiations
from collections import namedtuple

from selenium import webdriver
import xml.etree.ElementTree  as ET
from libconifgs import mylibs

data_file="quoraxml.xml"

obj = namedtuple('obj', 'root, browz, url')

#main function where the application starts
if __name__ == '__main__':
  
    quora_cl = mylibs()
    #Getting XML's root
    obj.root = quora_cl.getRoot(data_file)
    #print(obj.root)
    
    #Initialising browser
    #obj.browz=quora_cl.getBrowser("C:\Temp\src\IEDriverServer_x64\IEDriverServer", "Ie")
    #print(obj.browz)

    print(quora_cl.readXML(obj.root))

