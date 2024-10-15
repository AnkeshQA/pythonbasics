from utilities.configurations import *
config = getconfig()

from utilities.resources import *


import requests

url = "https://github.com/login"

github_response = requests.get(url,verify=False,auth=('ashikhar6@gmail.com',getPassword()))
print(github_response.status_code)

#rewatch lecture 34 to use in authentication