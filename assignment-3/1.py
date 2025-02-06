num=int(input("Enter number:"))
digital_root=0
while num!=0:
    while num!=0:
       q=num%10
       num=num//10
       digital_root+=q
    if digital_root>9:
        num=digital_root
        digital_root=0
print(digital_root)
