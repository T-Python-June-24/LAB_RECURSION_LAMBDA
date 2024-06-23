list1 = [40, 35, 10, 15, 20]
list2 = lambda x: x*x

y = map(list2,list1)

print(list(y))