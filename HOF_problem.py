'''
you will  be given a list .. find the odd numbers sum, even numbers sum and the numbers those are divisible by 3 there sum..
solving it with Higher order function(those function are called HOF if they recieve function as a input) and lambda function
'''
def return_sum(func, L):
    result =0 
    for i in L:
        if func(i):
            result= result+ i
    
    return result



L= [11,14,15,17,90,21,24]

x= lambda x: x%2==0
y= lambda x: x%2!=0
z= lambda x: x%3==0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))