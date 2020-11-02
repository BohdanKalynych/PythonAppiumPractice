import json
import requests

response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
json_dict = json.loads(response.text)


print(json_dict['data'][0]['employee_name'])
print(len(json_dict['data']))

saved_names =[]
for x in range(len(json_dict['data'])):
    saved_names.append(json_dict['data'][x]['employee_name'])

print(saved_names)

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
# print(people[1]['name'])