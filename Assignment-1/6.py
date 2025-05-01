list=[]
dist=[]
for i in range(10):
    print(f"Enter {i+1} point:")
    x=int(input("Enter your x coefficient:"))
    y=int(input("Enter your y coefficient:"))
    z=int(input("Enter your z coefficient:"))
    list.append((x,y,z))
for i in range(10):
    temp=[]
    for j in range(10):
        if i!=j:
            sum=0
            for k in range(3):
                sum+=(int(list[i][k]))-int(list[j][k])**2
            temp.append(sum)
    min=temp[0]
    if i==0:
        k=1
    else:
        k=0
    for j in range(0,10-1):
        if min>temp[j]:
            min=temp[j]
            if j>=i:
                k=j+1
            else:
                k=j
    dist.append((list[i],list[k]))
print(list)
print(dist)