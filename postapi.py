# add the book method
# delete the book using post method
# data is used as params here in post method
# refer the document https://requests.readthedocs.io/en/latest/
import requests
from payload import *
#created a function payload.py and imported the details so that unique id will be created & automatically it will updated

from apirequest import response

add_book_response = requests.post(
    'http://216.10.245.166/Library/Addbook.php',
    json=addBookPayload("fefrewe"),  # Call the function and use its return value directly
    headers={"Content-Type": "application/json"}
)

print(add_book_response.json())
response_json = add_book_response.json()
print(type(add_book_response.json()))
bookID = response_json['ID']

#delete the book
response_delete_book = requests.post('http://216.10.245.166/Library/DeleteBook.php',json={
    "ID" : bookID
},headers={"Content-Type":"application/json"},)
assert response_delete_book.status_code == 200
confirm_json = response_delete_book.json()
print(confirm_json["msg"])
assert confirm_json["msg"] =="book is successfully deleted"