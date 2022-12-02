with open("input.txt", "r") as file:
    lines = file.read().splitlines()
file.close()
points = [("A X", 4), ("A Y", 8), ("A Z", 3), ("B X", 1), ("B Y", 5), ("B Z", 9), ("C X", 7), ("C Y", 2), ("C Z", 6)]
points2 = [("A X", 3), ("A Y", 4), ("A Z", 8), ("B X", 1), ("B Y", 5), ("B Z", 9), ("C X", 2), ("C Y", 6), ("C Z", 7)]
counter = 0
counter2 = 0
for line in lines:
    for point in points:
        if (point[0] == line):
            counter += point[1]
    for point2 in points2:
        if (point2[0] == line):
            counter2 += point2[1]    
print(counter, counter2)
