import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset"

table = "FP001"
format = "JSON-stat/2.0/en"

def getAll():
    response = requests.get(url + "/"+table +"/"+format)

    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()
    

if __name__ == "__main__":
    with open("data\cso.json", "wt") as fp:
        #Write the data to a file in the data folder
        json.dump(getAll(), fp)
    print("Data written to file ")         
    