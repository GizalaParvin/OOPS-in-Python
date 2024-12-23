#del function in oops
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Gizala")
print(s1.name)
del s1.name
 

#Private and public method
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass= acc_pass
acc1 = Account(12321,37368)
print(acc1.acc_no)
print(acc1.acc_pass)

#private method
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass= acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
acc1 = Account(12321,37368)
print(acc1.acc_no)
print(acc1.acc_pass)

