numbers=[]
for i in range(1,10001):
    numbers.append(i)
rem_0=[]
rem_1=[]
rem_2=[]
rem_3=[]
rem_4=[]

for i in numbers:
    a=i%5
    match a:
        case 0:
            rem_0.append(i)
        case 1:
            rem_1.append(i)
        case 2:
            rem_2.append(i)
        case 3:
            rem_3.append(i)
        case 4:
            rem_4.append(i)

print("Equivalence classes for modulo 5:")
print(f"remainder:0\n {rem_0}")
print(f"remainder:1\n {rem_1}")
print(f"remainder:2\n {rem_2}")
print(f"remainder:3\n {rem_3}")
print(f"remainder:4\n {rem_4}")