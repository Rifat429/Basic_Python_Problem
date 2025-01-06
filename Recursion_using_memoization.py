import time
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]= memo(m-1,d)+ memo(m-2,d)
        return d[m]
start= time.time()
d = {0:1,1:1}
month = int(input("Enter your monther: "))
print(memo(month,d))

print(time.time()-start)