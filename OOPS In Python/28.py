class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"Your avg score is:",sum/3)
s1 =Student("tony sharks", [98,99,97])
s1.get_avg()