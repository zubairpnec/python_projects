#check class
#class number: 1
class one: #doesnt take any input, prints a welcome message
    def __init__(self): #constructor
        pass

    def greet(self):
        print("\nWelcome to the company")

#---------------------------------------------------------------------------
# input argument
#class number: 2
class two(): #Take an input, prints a welcome message
    def __init__(self,org_name): #constructor
        self.name = org_name

    def greet(self): #polymorphism: same greet method, differently in different classes
        print("\nYou are welcomed to the organization: ",self.name)

#-------------------------------------------------------------------------
#inherits properties and over rides a method
#class number: 3
class three(two): #inherits the class two, over rides the greeting method

    def greet(self):
        print("\nThe greeting message has been over-ridden. The input provided is: ",self.name)

#--------------------------------------------------------------------------
#class number 4:
class four(two):
    def __init__(self,name): #re-defining the constructor. will no longer inherit all properties of parent.
        self.name = str.upper(name)

    #not going to change the greeting message

#--------------------------------------------------------------------------
#class number: 5
class five(two): #inherits the class two, over rides the greeting method

    def __init__(self,name):
        self.name = name
        print("\nIm fifth class constructor ")
    def greet(self,year): #method over-loading. New implementation of a method but not necessarily the same inputs
        print("Welcome to the organization: ",self.name, ". It was founded in: ",year)

class six(five):
    def __init__(self,organization):
        #five.__init__(self,organization) #inherits the properties
        super().__init__(organization)  #super method, an alternative



if __name__ == "__main__":
    obj1 = one()
    obj1.greet()

    obj2 = two("SUPARCO")
    obj2.greet()

    obj3 = three("NESCOM")
    obj3.greet()

    obj4 = four("atomic energy")
    obj4.greet()

    obj5 = five("ISRO")
    obj5.greet(1962)

    obj6 = six("ESA")
    obj6.greet(1958)