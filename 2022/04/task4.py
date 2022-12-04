import re
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
counter = 0
counter2 = 0
for line in lines:
    tmp=re.split('-|,',line)
    first = set(range(int(tmp[0]), int(tmp[1]) + 1))
    second = set(range(int(tmp[2]), int(tmp[3]) + 1))
    if (first.issubset(second) | second.issubset(first)):
        counter += 1
    if (first & second):
        counter2 += 1
print (counter, counter2)