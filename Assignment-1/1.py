
#list of numbers from 0 to 49
num=[]
for i in range(50):
    num.append(i)
print(num)

#squares of integers from 1 to 50
square=[]
for i in range(51):
    square.append(i**2)
print(square)

#list containing ['a','bb',.....]
a=[]
for i in range(26):
    a.append(chr((ord('a')+i))*(i+1))
print(a)
