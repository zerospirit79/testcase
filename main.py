import requests
import json
from collections import ChainMap


first_method = 'sisyphus'
request_url_sisyphus = 'https://rdb.altlinux.org/api/export/branch_binary_packages/' + first_method
response_sisyphus = requests.get(request_url_sisyphus).text
sisyphus_dict = json.loads(response_sisyphus)
sisyphus_dictionary = sisyphus_dict['packages']
print(sisyphus_dictionary)

second_method = 'p10'
request_url_p10 = 'https://rdb.altlinux.org/api/export/branch_binary_packages/' + second_method
response_p10 = requests.get(request_url_p10).text
p10_dict = json.loads(response_p10)
p10_dictionary = p10_dict['packages']

p10_diff = []
sisyphus_diff = []

for obj in sisyphus_dictionary:
    for data in p10_dictionary:
        if obj['name'] != data['name']:
            p10_diff.append(obj)
            break
        else:
            break

for obj in p10_dictionary:
    for data in sisyphus_dictionary:
        if obj['name'] != data['name']:
            sisyphus_diff.append(obj)
            break
        else:
            break


filename = 'p10_diff.json'
with open(filename, 'w') as f:
    json.dump(p10_diff, f)

filename = 'sisyphus_diff.json'
with open(filename, 'w') as f:
    json.dump(sisyphus_diff, f)

'''
for name in data_collection():
    p10_diff = []
    sisyphus_diff = []
    if name.p10_dictionary != name.sisyphus_dictionary:
        p10_diff.append(name.p10_dictionary)
        print(p10_diff)
    elif sisyphus_dictionary['name'] != p10_dictionary['name']:
        sisyphus_diff.append(sisyphus_dictionary['name'])
        print(sisyphus_diff)

'''