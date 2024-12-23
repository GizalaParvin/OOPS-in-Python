#formal function/ long method
numbers = [11,20,31,40,51,60,90,59,90]
def even(x):
    return x % 2 == 0
evens =list(filter(even,numbers))
print("Even numbers:",evens)

#lembda function
numbers = [11,20,31,40,51,60,90,59,90]
evenn = list(filter(lambda x : x % 2==0 and x>50,numbers))
print("Even numbers greater than 50:",evenn)


city =['jaipur','kota','chandigarh','delhi','Muzaffarpur']
sort =sorted(city,key=lambda x: len(x),reverse=True)
print("Sorted words by lenght:",sort)
