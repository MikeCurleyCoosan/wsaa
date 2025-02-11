import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

#print (doc.toprettyxml(newl='')) #output to console


objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

for objTrainPositionNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

    # now lets get everything
    dataList = []
    flag = False
    for retrieveTag in retrieveTags:
        datanode = objTrainPositionNode.getElementsByTagName(retrieveTag).item(0)
        print(f"Train Object tags are {retrieveTag}")
        dataList.append(datanode.firstChild.nodeValue.strip())
        # this print shows each line being incrementally built
        print(f"{dataList}")
        # only store train codes beginning with 'D'
        if retrieveTag == 'TrainCode' and datanode.firstChild.nodeValue[0] == 'D':
            flag = True
    