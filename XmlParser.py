import pandas as pd
import xml.etree.cElementTree as et

parsedXML = et.parse( "input.xml" )
dfcols = ['name','email','phone','street']
df = pd.DataFrame(columns=dfcols)

def getvalueofnode( node ):
    return node.text if node is not None else None

for node in parsedXML.getroot():
    name = node.attrib.get('name')
    email = node.find('email')
    phone = node.find('phone')
    street = node.find('address/street')
    df = df.append( pd.Series(
        [name, getvalueofnode(email), getvalueofnode(phone), getvalueofnode(street)],
        index=dfcols) ,ignore_index=True)
print(df)

import xmltodict

xmlDict = xmltodict.parse( "input.xml" )
#df = pd.DataFrame.from_dict(xmlDict)