# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "Mizo", "last_name": "Abousaid", "age": 25}'

# Parse to dict
user = json.loads(userJSON)
# print(user['first_name'])
# print(user)

car = {'mark': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)