'''
Script for inferencing the deployed model
'''

import json 
import requests

data = [[-117,   33,   24, 4365,  804, 2663,  753,    4,   0],
       [-121,   38,   19, 3326,  561, 1544,  511,    2,    1],
       [-117,   34,   18, 2127,  443, 1168,  401,    3,    1],
       [-118,   34,   23, 3098,  542, 1486,  492,    5,    0],
       [-121,   40,   17, 2816,  639, 1027,  406,    2,    1]]

url = 'http://127.0.0.1:8000/predict/'

predictions = []
for record in data:
    #record = data[1]
    payload = {'features': record}
    payload = json.dumps(payload)
    response = requests.post(url, data=payload)
    predictions.append(response.json()['predicted_class'])

print(predictions)




