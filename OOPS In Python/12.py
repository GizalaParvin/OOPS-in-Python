marks =[ 77,97,56,87,95]

def grade(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks < 90:
        return  'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks <70:
        return 'D'
    else:
        return 'F'
    
grades =map(grade,marks)# we can also use list command here to print all the grade at once like #grades=list(map(grades,marks))

print("Exam Scores:",marks)
print("Grades:", next(grades))
#print("Grades:", next(grades))
print("Grades:",list(grades))    

#    
