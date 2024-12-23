# Example Program for Private data Member and Access By Public Method 


#Creating a class
class Employee:
    #Constructor
    def __init__(self,name,salary):
        self.name = name  #name is a Public Member
        self.__salary = salary  #Salary is Private Member __
    def show(self):
        return(f"Name = {self.name}, Salary={self.__salary}")

#Object Creation    
e1 = Employee("amit",100000)  

#This statement prints the Name since Name is a Public Member
print(e1.name)

#The following statement throws an attribute error since private member of the class
#cant be access from outside of the class

#print(e1.__salary) # some error has occured in the pdf of this line 


#Acessing Private member Of the class by a Public method

print(e1.show())