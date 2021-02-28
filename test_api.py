import requests
import json


input_data = {"body": "The sky is blue and beautiful. Love this blue and beautiful sky!The quick brown fox jumps over the lazy dog."}

url = ""

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())














