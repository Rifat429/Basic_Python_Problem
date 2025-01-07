import functools
L=[10,12,20,10]

print(functools.reduce(lambda x,y: x+y, L))

### find the biggest number from a list using reduce...

print("The biggest number of the list",functools.reduce(lambda x,y: x if x>y else y,L))


## find the lowest

print("The lowest number of the list",functools.reduce(lambda x,y: y if x>y else x,L))