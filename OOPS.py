# what classes ?
# ans:- classes are nothing but blueprint or prototype
# sum, multiply, addition, constant
# it will have methods, variables, instance variable, constructors
# class can have variable and methods

# declaring classes in python
class Calculator:
    num = 100

    def getData(self):
        print("I am now executing as methods in class")

# calling the method outside of the class
# create object of any class
obj = Calculator() #syntax to create objects in python
obj.getData()
print(obj.num)


# constructor is one method when you create object for any class. Iss just for any object.
# If we don't define anything then default constructor will be called

