num=int(input("Enter number:"))
reverse_num=0
while num>0:
    i=num%10
    reverse_num=reverse_num*10+i
    num=num//10

print("Reversed number is",reverse_num)