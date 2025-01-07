'''why we should learn iterator'''
import sys

l= [x for x in range(1,1000)]
# for x in l:
#     print(x*2)

print(sys.getsizeof(l)/1024)###it will take 8.6484375 MB
x=range(1,1000)
print(sys.getsizeof(x)/1024)### it will take only 0.0046875 MB


L =[1,2,3]
print(type(L)) ##L is a iterable 

##iter(L)--> is a iterator
print(type(iter(L))) ##tytpe will be list_iterator..



t=(1,2,3)
print(dir(t))##finding if a object is iterable or not..if __iter__ method is showing then the object is iterable 

## making an iterator from an Iterable
item = iter(t)
print(dir(item)) ## now we will have __iter__ + __next__ method here..so it is a iterator...