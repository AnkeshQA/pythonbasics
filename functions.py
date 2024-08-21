# function is group of statement that perform specific task
#def :- identifier

#Function Declaration
def GreetMe():
    print("Good Morning")
    # function call
GreetMe()


#parameterized function

def GreetMe(name):
    print("Good Morning" + name)
    # function call
GreetMe("Ankesh Shikhar")


 #function of two integers
def add(a, b):
    result = a + b
    return result

print (add(5, 4))
