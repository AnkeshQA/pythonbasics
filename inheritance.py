# inheritance is acquiring properties of parent class into child class
# create a class and in bracket add parent class name from which u want to inherit. And it gives access to child class
from constructor import Calculator


class ChilInhr(Calculator):
    num2 = 200

    def __init__(self):
# calling the parent constructor in child constructor
        Calculator.__init__(self, 2,2)


    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChilInhr()
# this will fail because it requires two positional arguments a,b need to use constructor.
# check for constructor declaration in parent class

print(obj.getCompleteData())