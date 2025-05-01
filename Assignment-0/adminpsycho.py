n=int(input("Enter number of employees:"))
a=[]
for i in range(n):
    element=int(input(f"enter the empolyee {i+1}:"))
    a.append(element)
print("List:",a)
swap=0   
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    if min!=i:
        swap+=1
        a[i],a[min]=a[min],a[i]
print("Sorted lists:",a)
print("Minimum swaps:",swap)
