# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

# student1 = Student("Alice",15,"9th")
# student2 = Student("Bob",14,"10th")

# print("Student 1: ")
# print("Name ",student1.name)
# print("Age",student1.age)
# print("Grade",student1.grade)

# print("Student 2: ")
# print("Name ",student2.name)
# print("Age",student2.age)
# print("Grade",student2.grade)

# class Students:
#     pass

# # Creating an instance of the class
# students_instance = Students()

# # Checking the type of the instance
# print("Type of students_instance:", type(students_instance))

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car = Vehicle(30,50)
bike = Vehicle(89,90)
print("Car - Max speed: ",car.max_speed , "Car Mileage: ",car.mileage)
print("Bike - Max speed: ",bike.max_speed , "Bike Mileage: ",bike.mileage)


