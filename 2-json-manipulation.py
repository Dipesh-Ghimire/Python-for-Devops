import json

json_data = '{"name":"dipesh","age":22,"city":"Kathmandu"}'

data_dict = json.loads(json_data)

data_dict['country'] = 'Nepal'

new_json_data = json.dumps(data_dict)

print(type(new_json_data))

# write to json file
# with open("output.json","w") as file_obj:
#     json.dump(data_dict,file_obj)

# write to json file
with open("data.json","r") as file_obj:
    xyz = json.load(file_obj)

print(type(xyz))