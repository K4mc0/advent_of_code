with open("input.txt", "r") as file:
    lines = file.read().splitlines()
file.close()
max = 0
tmp = 0
array = []
for line in lines:
    if(line == ""):
        array.append(tmp)
        if (tmp > max):
            max = tmp
        tmp = 0
    else:
         tmp += int(line)
array.sort(reverse=True)
#task 1
print(max)
#task 2
print (array[0]+array[1]+array[2])