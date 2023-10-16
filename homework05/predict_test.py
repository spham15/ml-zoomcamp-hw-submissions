import requests


url = 'http://localhost:9696/predict'

client_id = 'xyz-123'
# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
client = {"job": "retired", "duration": 445, "poutcome": "success"}


response = requests.post(url, json=client).json()
print(response)

if response['credit'] == True:
    print('giving credit to %s' % client_id)
else:
    print('not giving credit to %s' % client_id)