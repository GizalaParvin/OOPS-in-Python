class Employee:
    def __init__(self,name,salary,project):
        self.name =name
        self.__salary=salary
        self._project =project
    def show(self):
        print("NAme=",self.name,"salary=",self.__salary)
    def getsalary(self):
        return(self.__salary)
E1=Employee("Amit",2000,"NLP")
#print(E1.getsalary())
print(E1.show())    
