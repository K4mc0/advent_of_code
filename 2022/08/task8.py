with open("input.txt", "r") as file:
    lines = file.read().splitlines()
test = """30373
25512
65332
33549
35390"""

#lines = test.splitlines()

def visible_left(matrix, x, y):
    if (x == 0):
        return True
    for i in range(0, x):
        if (int(matrix[y][x]) <= int(matrix[y][i])):
            return False
    return True

def visible_right(matrix, x, y):
    if (x == len(matrix[y])):
        return True
    for i in range(x+1, len(matrix[y])):
        if (int(matrix[y][x]) <= int(matrix[y][i])):
            return False
    return True

def visible_up(matrix, x, y):
    if (y == 0):
        return True
    for i in range(0, y):
        if(int(matrix[y][x]) <= int(matrix[i][x])):
            return False
    return True

def visible_down(matrix, x, y):
    if (y == len(matrix)):
        return True
    for i in range(y+1, len(matrix)):
        if(int(matrix[y][x]) <= int(matrix[i][x])):
            return False
    return True

def score_left(matrix, x, y):
    score = 0
    if (x == 0):
        return score
    for i in range(x-1, -1, -1):
        score += 1
        if (int(matrix[y][x]) <= int(matrix[y][i])):
            return score
    return score

def score_right(matrix, x, y):
    score = 0
    if (x == len(matrix[y])):
        return score
    for i in range(x+1, len(matrix[y])):
        score += 1
        if (int(matrix[y][x]) <= int(matrix[y][i])):
            return score
    return score

def score_up(matrix, x, y):
    score = 0
    if (y == 0):
        return score
    for i in range(y-1, -1, -1):
        score += 1
        if (int(matrix[y][x]) <= int(matrix[i][x])):
            return score
    return score

def score_down(matrix, x, y):
    score = 0
    if (y == len(matrix)):
        return score
    for i in range(y+1, len(matrix)):
        score += 1
        if (int(matrix[y][x]) <= int(matrix[i][x])):
            return score
    return score

counter = 0
score = 0
best_score = 0
y = 0
for line in lines:
    for x in range(0, len(line)):
        if (visible_left(lines, x, y) or visible_right(lines, x, y) or visible_up(lines, x, y) or visible_down(lines, x, y)):
            counter += 1
        score = score_left(lines, x, y) * score_right(lines, x, y) * score_up(lines, x, y) * score_down(lines, x, y)
        if (score > best_score):
            best_score = score
    y += 1
print ("Result for task 1", counter)
print ("Result for task 2", best_score)