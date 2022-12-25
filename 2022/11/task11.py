import re
import time

class Monkey(object):

    def __init__(self, items, operation, test, true, false):
        self.items = items  
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0

    def do_operation(self, old, relief):
        self.inspections += 1
        if (self.operation.split(" ")[5] == "old"):
            left = old
        if (self.operation.split(" ")[7] == "old"):
            right = old
        else: right = int(self.operation.split(" ")[7])
        if (self.operation.split(" ")[6] == "+"):
            if(relief):
                return (left + right) // 3
            else: return (left + right)
        if (self.operation.split(" ")[6] == "*"):
            if(relief):
                return (left * right) // 3
            else: return (left * right)
    
    def do_test(self, input):
        if (input % self.test == 0):
            return self.true
        else: return self.false
    
    def add_item(self, item):
        self.items.append(item)
    
    def clear_items(self):
        self.items.clear()
    
def iniciate_monkeys():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    monkeys = []
    starting_items, test, true, false, operation = [], 1, 1, 1, ""
    for line in lines:
        if (not line.strip()):
            monkeys.append(Monkey(starting_items, operation, test, true, false))
            starting_items, test, true, false, operation = [], 1, 1, 1, ""
        elif (line.__contains__("Starting")):
            tmp = re.split(": |, ", line)
            tmp.pop(0)
            for i in range(len(tmp)):
                starting_items.append(int(tmp[i]))
        elif (line.__contains__("Operation")):
            operation = line
        elif (line.__contains__("Test")):
            test = int(line.split(" ")[5])
        elif (line.__contains__("true")):
            true = int(line.split(" ")[9])
        elif (line.__contains__("false")):
            false = int(line.split(" ")[9])
    monkeys.append(Monkey(starting_items, operation, test, true, false))
    return monkeys

def solution(monkeys, rounds, relief):
    for round in range(rounds):
        for monkey in range(len(monkeys)):
            for item in range(len(monkeys[monkey].items)):
                x = monkeys[monkey].do_operation(monkeys[monkey].items[item], relief)
                monkeys[monkeys[monkey].do_test(x)].add_item(x)
            monkeys[monkey].clear_items()
    score = []
    for monkey in range(len(monkeys)):
        score.append(monkeys[monkey].inspections)
    score.sort(reverse=True)
    return score[0] * score[1]

def main():
    monkeys = iniciate_monkeys()
    print("Result for task 1 is", solution(monkeys, 20, True))
    monkeys = iniciate_monkeys()
    start_time = time.time()
    print("Result for task 2 is", solution(monkeys, 10000, False))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()