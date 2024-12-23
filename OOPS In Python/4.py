#Constructor method
class faculty:
    def __init__(self):
        self.id =int(input("Enter the Id: "))
        self.name =input("Enter the name: ")
        self.salary=float(input("Enter the salary of faculty: " ))
    def display(self):
        print("Employee Id:",self.id)   #print(f"Employee Id: {self.Name} has a id {self.id} and has a salary {self.salary}")
        print("Employee name:",self.name)
        print("Employee salary",self.salary)    

a=faculty()
a.display()
b=faculty()
b.display()