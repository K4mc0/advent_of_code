def is_touching(xH, xT, yH, yT):
    if(xH == xT or xH == xT - 1 or xH == xT+1):
        if(yH == yT or yH == yT - 1 or yH == yT+1):
            return True
    return False

def make_move(direction, xH, xT, yH, yT, head):
    if (head):
        if (direction == 'L'):
            xH -= 1
        elif (direction == 'R'):
            xH += 1
        elif (direction == 'U'):
            yH += 1
        elif (direction == 'D'):
            yH -= 1
    if (not is_touching(xH, xT, yH, yT)):
        if (xH == xT):
            if (yT == yH + 2 ):
                yT -= 1 
            elif (yT == yH - 2):
                yT += 1
        elif (yH == yT):
            if (xT == xH + 2 ):
                xT -= 1 
            elif (xT == xH - 2):
                xT += 1
        else:
            if (xH < xT):
                if (yH < yT):
                    xT -= 1
                    yT -= 1
                else:
                    xT -= 1
                    yT += 1
            else:
                if (yH < yT):
                    xT += 1
                    yT -= 1
                else:
                    xT += 1
                    yT += 1           
    return (xH, xT, yH, yT)

def solution(rope_length):
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    x = [0] * rope_length
    y = [0] * rope_length
    tail_moves = {(x[rope_length-1], y[rope_length-1])}
    head = True
    for line in lines:
        direction = line.split(" ")[0]
        moves = int(line.split(" ")[1])
        for i in range(moves):
            for j in range(rope_length-1):
                if (j == 0):
                    head = True
                else: head = False
                tmp = make_move(direction, x[j], x[j+1], y[j], y[j+1], head)
                x[j], x[j+1], y[j], y[j+1] = tmp[0], tmp[1], tmp[2], tmp[3]
            tail_moves.add((x[rope_length-1], y[rope_length-1]))
    return len(tail_moves)

def main():
    print("Result for task 1 is", solution(2))
    print("Result for task 2 is", solution(10))

if __name__ == "__main__":
    main()