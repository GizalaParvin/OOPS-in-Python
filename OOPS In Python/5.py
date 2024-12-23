# #Passing parameters(Long form)
class faculty:
    def __init__(self,a,b,c):
        self.id =a
        self.name =b
        self.salary=c
    def display(self):
        print("Employee Id:",self.id)   #print(f"Employee Id: {self.Name} has a id {self.id} and has a salary {self.salary}")
        print("Employee name:",self.name)
        print("Employee salary",self.salary)    

a=faculty(1,"varun",10000)
a.display()

#short form
class faculty:
    def __init__(self,a,b,c):
        self.id = a
        self.name =b
        self.salary = c
    def display(self):
        print(f"Faculty id  is : {self.id} and his name is {self.name} and his salary is {self.salary}")
a=faculty(1,"Varun",10000)
a.display()
