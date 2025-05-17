import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://<yoururl>.atlassian.net//rest/api/3/project"

API_TOKEN =  "put api token"

auth = HTTPBasicAuth("YourMailId", API_TOKEN) #better to have env varaible to token 

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output = json.loads(response.text) #here we are converting json to dictionary so we are using the json.load()
name = output[0]["name"]
print(name)