import requests
import json


input_data = {"body": 'Tesla is looking at buying U.S. startup for $6 million, is it ok?'}



url = "https://53wg3glwn0.execute-api.us-east-2.amazonaws.com/api_houseprice/predict"

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())



# key = {'x-api-key': 'tI95Zb3Ikr5l8jK1o3DDN4BOzFDLi13y3GYZ5uDW'}


# r = requests.post(url, json.dumps(input_data), headers=key)
# res = json.loads(r.content)
# print("result with securely key: ", res)













