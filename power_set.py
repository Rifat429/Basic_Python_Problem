def power_set(li,index=0, current=None):
    if current is None:
        current =[]
    if index == len(li):
        return [current[:]]

    if(len(li)==0):
        return [[]]

    exclude = power_set(li,index+1,current )

    current.append(li[index])
    include = power_set(li, index + 1, current)
    current.pop()  
    

    return exclude + include


li = [1,2,3]
print(power_set(li))


