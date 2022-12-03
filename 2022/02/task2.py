with open("input.txt", "r") as file:
    lines = file.read().splitlines()
file.close()
points = [("A X", 4, 3), ("A Y", 8, 4), ("A Z", 3, 8), ("B X", 1, 1), ("B Y", 5, 5), ("B Z", 9, 9), ("C X", 7, 2), ("C Y", 2, 6), ("C Z", 6, 7)]
counter = [0, 0]
for line in lines:
    for point in points:
        if (point[0] == line):
            counter[0] += point[1]
            counter[1] += point[2]  
print(counter[0], counter[1])