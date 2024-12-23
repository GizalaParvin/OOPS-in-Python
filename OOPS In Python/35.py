class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180

# Creating two objects of the Triangle class
T1 = Triangle(80, 30, 40)
T2 = Triangle(70, 50, 60)

# Checking the angles for T1
print(f"T1: {T1.check_angles()}")  # Should print: True

# Checking the angles for T2
print(f"T2: {T2.check_angles()}")  # Should print: False

class Souvenir:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

# Creating an object of the Souvenir class representing the book "OOPS" by "D. Mark" and published by "TMH"
souvenir_book = Souvenir("OOPS", "D. Mark", "TMH")

# Printing out the title, author, and publisher of the book
print(f"Title: {souvenir_book.title}")
print(f"Author: {souvenir_book.author}")
print(f"Publisher: {souvenir_book.publisher}")
