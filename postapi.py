# add the book method
# delete the book using post method
# data is used as params here in post method
# refer the document https://requests.readthedocs.io/en/latest/

from payload import *


#created a function payload.py and imported the details so that unique id will be created & automatically it will updated and deleted without any failure

from apirequest import response
# import configparser --> this is moved to configurations.py file

# import from configuration using import * which will import everything from configuration file
from utilities.configurations import *
config = getconfig()

#date :- 16/10/2024
#create an utilities file and add end point in properties file which has .ini extension
# then use import configparser and then follow below steps config = configparser.ConfigParser() & config.read('utilities/properties.ini') (moved to configuration file)
# config = configparser.ConfigParser()
# use the below property to read the path of the file
# use read method here
# config.read('utilities/properties.ini')

#Next step :- move from (import configparser till config.read('utilities/properties.ini') to configuration file

# (config['API']['endpoint']+ this will read endpoint from properties.ini file

#importing resources from utilities
from utilities.resources import *

import requests

url = config['API']['endpoint']+'/Library/Addbook.php' + Apiresources.addBook
headers = {"Content-Type": "application/json"}
add_book_response = requests.post(url,json=addBookPayload("fefrewe"), headers= headers,  # Call the function and use its return value directly
)
# move '/Library/Addbook.php' & '/Library/DeleteBook.php' to resouces.py file in utilities folder


print(add_book_response.json())
response_json = add_book_response.json()
print(type(add_book_response.json()))
bookID = response_json['ID']

#delete the book
url1 = config['API']['endpoint'] + Apiresources.deleteBook
headers={"Content-Type":"application/json"}
response_delete_book = requests.post(url1,json={"ID" : bookID},headers=headers,)
assert response_delete_book.status_code == 200
confirm_json = response_delete_book.json()
print(confirm_json["msg"])
assert confirm_json["msg"] =="book is successfully deleted"