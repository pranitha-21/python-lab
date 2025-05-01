name=[]
print("enter students names")
for i in range(2):
    name.append(str(input(f"{i+1}:")))

print("Displaying students namr(reverse)")
for i in name:
    reverse_name=i[:15]
    reverse_name=reverse_name[::-1]
    print(reverse_name)