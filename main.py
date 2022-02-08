import requests
import json

def printing(data):
    text = json.dumps(data, sort_keys=True, indent=8)
    print(text)

def p10_package(obj):


request_url_sisyphus = 'https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus'
response = requests.get(request_url_sisyphus)
sisyphus_json = response.json()

printing(sisyphus_json)

request_url_p10 = 'https://rdb.altlinux.org/api/export/branch_binary_packages/p10'
response = requests.get(request_url_p10)
p10_json = response.json()

printing(p10_json)


