# def addition(n1,n2):
# 	return(n1 + n2)
# def addition(n1,n2,n3):
# 	print(n1 + n2 + n3)
# print(addition(1,2,3))


class Book:
	def __init__(self,pages):
		self.pages = pages
		  
    def __add__(self,another):
	    return(self.pages + another.pages)
b1 = Book(500)
b2 = Book(300)

print("Total number of pages",b1 + b2)	
	 
	