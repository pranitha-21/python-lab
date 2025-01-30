#count
cnt=0
num=int(input("enter the number u want to search:"))
l=[1,7,10,9,7,1,2,6,5,6,10,1]
for i in l:
    if i==num:
        cnt+=1

print("No. of times",num,"has appeared is",cnt)