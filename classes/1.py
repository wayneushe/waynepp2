class Person:
    def __init__(self, name , age ,course):
        self.name= name
        self.age= age
        self.course=course



    def myFunction(self):
      print("Hello i am "+ self.name)  

s1=Person("Wayne",20,1) #(creating an instance of the person class)
s1.myFunction()   




class twomethods:
    def __init__(self):
        self.input = ""
    def getString(self):
        self.input = input()
    def printString(self):
        self.input = print(self.input.upper())
a  = twomethods()
a.getString()
a.printString()