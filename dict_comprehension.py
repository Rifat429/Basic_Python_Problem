dict={
    "Name": "Rifat",
    "Age":27,
    "Nationality":"BD"
}

dict2= {key:value for key,value in dict.items() if len(key)>3}

print(dict2)

## list to dictionary

L=[10,12,13]
### the number will be the key and the square of that number will be value

dict3={ item:item**2 for item in L}
print(dict3)

