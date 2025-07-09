# on libraries
import requests
import json 
import sys
if len(sys.argv) != 2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[50])

o=response.json()
for result in o["results"]:
    print(result["trackName"])