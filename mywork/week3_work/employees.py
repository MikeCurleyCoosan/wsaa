#Read data from an xml file and use the xml.dom.minidom module to parse the data
from xml.dom.minidom import parse

#Set the filename we want to read from
filename = "data/employees.xml"

# read file in two ways
doc = parse(filename)
# or
#with open(filename) as fp:
#    doc = parse(fp)

#Get the list of Employee nodes
emloyeeNodeList = doc.getElementsByTagName("Employee")

#print(len(emloyeeNodeList)) #Testing purposes
for employeeNode in emloyeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print (firstName)