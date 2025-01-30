#rsplit
l=[]
s='This is a Python program'
current_word=''
for i in s:
    if i==" ":
        l.append(current_word)
        current_word=""
    else:
        current_word+=i
l.append(current_word)
print(l)
