import requests
import json
#import pandas as pd


first_method = 'sisyphus'
request_url_sisyphus = 'https://rdb.altlinux.org/api/export/branch_binary_packages/' + first_method
response = requests.get(request_url_sisyphus)
sisyphus_text = response.text
sisyphus_dict=json.loads(sisyphus_text)
#print(sisyphus_dict['packages'])

second_method = 'p10'
request_url_p10 = 'https://rdb.altlinux.org/api/export/branch_binary_packages/' + second_method
response = requests.get(request_url_p10)
p10_text = response.text
p10_dict = json.loads(p10_text)
print(p10_dict['packages'])

