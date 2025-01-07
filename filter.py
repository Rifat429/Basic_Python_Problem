'''suppose you have a list...find the numbers that are greater than 2'''
l=[20,3,6,1,0]

print(list(filter(lambda x:x>2, l)))

fruits=["Mango","Banana","Guava","Orange"] ## find all those fruits where e is present

print(list(filter(lambda name:'e' in name,fruits)))