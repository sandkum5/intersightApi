import json
import requests
from intersight_auth import IntersightAuth

# Get the intersight_auth file from: https://github.com/movinalot/intersight-rest-api/blob/master/intersight_auth.py

# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename="</path/to/SecretKey.txt>",
    api_key_id="<api-key-id>",
)

# Intersight REST API Base URL
BASE_URL = "https://www.intersight.com/api/v1/"

# $select=Name filters the output and only returns Name. Intersight responds with the ClassId, Moid, ObjectType by default. 
url_path = "organization/Organizations?$select=Name"
payload = {}
headers = {}

response = requests.request(
    method="GET", url=f"{BASE_URL}{url_path}", auth=AUTH, headers=headers, data=payload
)

# Extract the Moid from the Results
json_result = json.loads(response.text)

# Iterate over the response list and print the Org Name,Moid,ClassId. 
for i in range(len(json_result["Results"])):
    Name = json_result["Results"][i]["Name"]
    Moid = json_result["Results"][i]["Moid"]
    ClassId = json_result["Results"][i]["ClassId"]
    print(f"Org_Name: {Name}")
    print(f"  Org_Moid: {Moid}")
    print(f"  Org_ClassId: {ClassId}")
    print("")
