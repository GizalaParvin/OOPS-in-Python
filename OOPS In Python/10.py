#using for loop
marks =[10,20,52,21,55]
new_marks =[]
for x in marks:
    new_marks.append(x+2)
print("using for loop:",new_marks)    


#using list comprehention
marks =[10,20,52,21,55]
new_marks =[x + 2 for x in marks]
print("using list comprehention:",new_marks)

#using list comprehention
easy =[x**3 for x in range(10) if x % 2 == 0]
print("using list comprehention: ",easy)

#using for loop 
cubes = []
for x in range(10):
    if x % 2 == 0:
        cubes.append(x**3)
print("using for loop: ",cubes)        

cubes = []
for x in range(10):
    if x % 2 