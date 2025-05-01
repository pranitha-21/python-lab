import random

numbers=[random.randint(0,1) for i in range (100)]
print(numbers)

longest_run=0
current_run=0
for i in numbers:
    if i==0:
        current_run +=1
    else:
        longest_run=max(longest_run,current_run)
        current_run=0



print(f"Longest run is {longest_run}")