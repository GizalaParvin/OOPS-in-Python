# Example Program for Access of Private data member by Name mangling

#Creating class
class Employee:
    #Constructor
    def __init__(self,name,salary):
        self.name =name
        self.__salary =salary

    #Instance Method(Private method can be  accesses By Public Function Of the class)
    def show(self): #Public Method
        return(f"Name = {self.name} , Salary ={ self.__salary}")  

    def getSalary(self):
        return(self.__salary) 

#Object creation
e1 =Employee("amit",10000)

#this statement prints the name since Name is a Public Member
print(e1.name)

#Accessing Private member of the class by name mangling
print("Printing private datamember values by name mangling ",e1._Employee__salary)

#Accessing Private member of the class by a public method
print(e1.getSalary())