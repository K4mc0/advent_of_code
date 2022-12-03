import string
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
file.close()
points = list(string.ascii_letters)
counter = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    common_character = ''.join(set(firstpart).intersection(secondpart))
    #print(common_character)
    counter += points.index(common_character)+1
print (counter)
#task 2
score = 0
for line in lines:
    if (lines.index(line) % 3 == 0):
        x = line
    if (lines.index(line) % 3 == 1):
        y = line
    if (lines.index(line) % 3 == 2):
        z = line
        score += points.index(''.join(set(x).intersection(y).intersection(z)))+1
print(score)