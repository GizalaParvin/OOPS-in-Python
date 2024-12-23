def creater1():
    i = 1
    while i <=200:
        yield i 
        i += 1

print(creater1())
x =creater1()
print(next(x))
print(next(x))
print(next(x))
print(list(x))
