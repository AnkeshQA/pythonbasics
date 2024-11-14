#dowload and install request library python via pycharm terminal
import json

import requests

#parameter and url is separated by "?" after "?" anything we have is a query parameter
# in case "/" is mentioned then it is form parameter
# get method will not have body to talk to the server
response = requests.get('http://216.10.245.166/Library/GetBook.php',params={'AuthorName':'Rahul Shetty'},)

#print(response.text)
#print(type(response.text))
# here output is a list [{"book_name":"Learn Appium Automation with Java","isbn":"bc23d","aisle":"22790"}]
# when we use loads method and co/p coming out as "[]" the again it converts dictionary to list
#dict_response = json.loads(response.text)
#print(type(dict_response))
#dict_response[0]['isbn']
#print(dict_response[0]['isbn'])

#another method to do it in easy manner
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])

# status of the response
print(response.status_code)
assert response.status_code == 200
# if failure comes here then we can report
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# retrieve the book details with ISBN RS201
for actual_book in json_response:
    #print(type(book))
    if actual_book['isbn'] == 'RS201':
        print(actual_book)
        break

expected_book =  {
        "book_name": "Learn Appium Automation with Java",
        "isbn": "RS201",
        "aisle": "2223"
    }
print(f"Actual: {actual_book}")
print(f"Expected: {expected_book}")

assert actual_book == expected_book

