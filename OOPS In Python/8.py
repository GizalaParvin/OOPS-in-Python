def creater():
    list =[]
    i = 1
    while i <= 200:
        list.append(i)
        i += 1
    return list
print(creater())

#short method
numbers =list(range(1,201))
print(numbers)