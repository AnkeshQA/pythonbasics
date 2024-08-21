# a,b these are instance variable
# these two new variable which is instance variable
# self keyword is mandatory for calling variable into method
# instance Variable & class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when u create an object




class Calculator:
    num = 100
# class variable. can create n number of variable for a class
    def __init__(self,a,b):
        self.a = a
        self.b = b

        print("i am called automatically when object is created")
# init is a keyword to declare constructor in python

    def getData(self):
        print("I am now executing as methods in class")

    def summation(self):
        return self.a + self.b + Calculator.num
# here value should come from runtime which is constructor.
# class name which calculator.num as its independent
# u can also create using self.num


# calling the method outside of the class
# create object of any class
obj = Calculator(2,3)
# syntax to create objects in python
# here 2,3 will reach constructor first. If not it will throw an error.
obj.getData()
print(obj.summation())


obj1 = Calculator(4,5)
#syntax to create objects in python
obj1.getData()
print(obj1.summation())


# constructor is one method when you create object for any class. Iss just for any object.
# If we don't define anything then default constructor will be called