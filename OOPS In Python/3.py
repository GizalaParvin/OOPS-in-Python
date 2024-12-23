class Employee: #method1
    def putdata(self):
        self.id =int(input("Enter the id number: "))
        self.Name = input("Enter the name of employee ")
        self.salary =float(input("Ente the salary "))
    def display(self): #method 2
        print(f"Employee Id: {self.Name} has a id {self.id} and has a salary {self.salary}")
        # print("Employee Id:",self.id)   print(f"Employee Id: {self.Name} has a id {self.id} and has a salary {self.salary}")
        # print("Employee name:",self.Name)
        # print("Employee salary",self.salary)
a =Employee()
a.putdata()
a.display()
b =Employee()
b.putdata()
b.display()

