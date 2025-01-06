
def multiplication(a,n):
    if n==1:
        return a
    else:
        return a+multiplication(a,n-1)


print(multiplication(5,4))