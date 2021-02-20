import requests
import json


input_data = {"body": "The sky is blue and beautiful. Love this blue and beautiful sky!The quick brown fox jumps over the lazy dog."}

url = "https://q0cl1wwzb7.execute-api.us-east-2.amazonaws.com/dev/spacy"

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())



# key = {'x-api-key': 'tI95Zb3Ikr5l8jK1o3DDN4BOzFDLi13y3GYZ5uDW'}


# r = requests.post(url, json.dumps(input_data), headers=key)
# res = json.loads(r.content)
# print("result with securely key: ", res)













