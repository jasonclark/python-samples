import requests
import json
import base64


try:
    url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run'
    params = {
            'url': 'https://www.jasonclark.info/',
            'requestScreenshot': 'true',
            'key': "ADD-YOUR-API-KEY-HERE"
        }
    x = requests.post(url, data = params)
    data = json.loads(x.text)  
    with open("Finalscreenshot.png", "wb") as fh:
        fh.write(base64.b64decode(data["screenshot"]["data"]))
        print("Response code for Google Smartphone is " + str(x)[len(str(x))-5:len(str(x))-2])
        print("Page is " + data["mobileFriendliness"])
        
        if data["mobileFriendliness"] == "NOT_MOBILE_FRIENDLY":
            for iteration in range (len(data["mobileFriendlyIssues"])):
                print("The page has problems with " + str(data["mobileFriendlyIssues"][iteration]["rule"]))
        
        issues = data.get("resourceIssues", 0)
        if issues != 0:
            for iteration in range (len(data["resourceIssues"])):
                print("Problems with the blocked resources " + str(data["resourceIssues"][iteration]["blockedResource"]["url"]))
 
        print("Screenshot from " + str(params["url"]) + " is taken and downloaded.")
except:
    print("Problem with " + str(params["url"]) + ". " + str(x)[len(str(x))-5:len(str(x))-2] + " Response Code.")
