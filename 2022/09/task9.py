def is_touching(xH, xT, yH, yT):
    if(xH == xT or xH == xT - 1 or xH == xT+1):
        if(yH == yT or yH == yT - 1 or yH == yT+1):
            return True
    return False

def make_move(command, xH, xT, yH, yT):
    print("Head:", xH, yH, "Tail:", xT, yT)
    tail_moves = {(xT, yT)}
    direction = command.split(" ")[0]
    moves = int(command.split(" ")[1])
    for i in range(moves):
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
        tail_moves.add((xT,yT))
        print (i, "move", direction, "Head:", xH, yH, "Tail:", xT, yT)  
    print (moves, "moves", direction, "Head:", xH, yH, "Tail:", xT, yT)                
    return (xH, xT, yH, yT, tail_moves)

def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    xH, xT, yH, yT = 0, 0, 0, 0
    tail_moves = {(xT, yT)}
    for line in lines:
        tmp = make_move(line, xH, xT, yH, yT)
        print(tmp)
        xH, xT, yH, yT = tmp[0], tmp[1], tmp[2], tmp[3]
        for t in tmp[4]:
            tail_moves.add(t)
    print(len(tail_moves))
    if (is_touching(4,3,0,1)):
        print ("ano")
    else: print("nie")

if __name__ == "__main__":
    main()