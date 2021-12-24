#API scrape to get JSON file of MSPs
import requests
import json


response = requests.get("https://data.parliament.scot/api/members")


def jprint(obj):
    # create a formatted string of the Python JSON object
    jsonString = json.dumps(obj, sort_keys=True, indent=4)
    print(jsonString)
    jsonFile = open("sheet2.json", "w")
    jsonFile.write(jsonString)
    
jprint(response.json())
