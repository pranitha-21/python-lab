a="abcdgcdhi"
sub='cd'
for i in range(len(a)-len(sub)+1):
    if a[i:i+len(sub)]==sub:
        rindex=i
print(rindex)