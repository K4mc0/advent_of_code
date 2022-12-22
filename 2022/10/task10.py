def solution():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    cycle, x, result = [1], 1, 0
    for line in lines:
        if(line == "noop"):
            cycle.append(x)
        else:
            cycle.append(x)
            x += int(line.split(" ")[1])
            cycle.append(x)
    result = cycle[19]*20 + cycle[59]*60 + cycle[99]*100 + cycle[139]*140 + cycle[179]*180 + cycle[219]*220
    for i in range(len(cycle)):
        if (i % 40 == 0):
            print ()
        if (i % 40 == cycle[i] or i % 40 == cycle[i] +1 or i % 40 == cycle[i] - 1):
            print("#", end="")
        else: print("_", end="")
    return result

def main():
    print("\nResult for task 1 is", solution())

if __name__ == "__main__":
    main()