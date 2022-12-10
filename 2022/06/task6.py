with open("input.txt", "r") as file:
    input = file.read()
test = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"#7

def do_the_trick(str, num):
    queue = []
    for i in range(num):
        queue.append(str[i])
    for i in range(num,len(str)):
        tmp = set(queue)
        if(len(queue) == len(tmp)):
            return i
        else:
            queue.pop(0)
            queue.append(str[i])

print("And the winner is... ", do_the_trick(input, 14)) #4 for task 1, 14 for task 2