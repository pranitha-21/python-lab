a='abcdefg'
replace='ghi'
print("Enter indexs you want to replace ")
start=int(input("Enter the starting index:"))
end=int(input("Enter ending index:"))
r=list(a)
l=list(replace)
for i in range(start,end+1):
    if i-start<len(l):
        r[i]=l[i-start]

string_final=''
for i in r:
    string_final +=i

print(string_final)