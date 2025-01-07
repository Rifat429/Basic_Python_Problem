num = [1,2,3]

for i in num:
    print(i) ## this is a simple for loop..

##how it does it..
##first step..as num is iterable...we will fetch the iterator..
iter_num= iter(num)

###using the iterator it calls the next function....
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
