s=input()
a=set("abcdefghijklmnopqrstuvwxyz")
s=s.lower()
x=set(s)
x.remove(" ")
if x==a:
    print("pangram")
else :
    print("not pangram")
