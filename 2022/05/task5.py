with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def prepare_result(input):
    result = ""
    for k in range(9):
        result += cont[k][0]
    return result

#parsing of fancy input    
containers = lines[0:8]
moves = lines[10:len(lines)]
containers = [''.join(s) for s in zip(*containers)]
containers = [ x for x in containers if "[" not in x ]
containers = [ x for x in containers if "]" not in x ]
containers = [item.replace(' ','') for item in containers]
containers = [item for item in containers if item]

#create list stacks from list of strings
cont = []
for c in containers:
    tmp = []
    for j in c:
        tmp.append(j)
    cont.append(tmp)
cont2 = cont

#here the fun begins
""""
for move in moves:
    x = [int(s) for s in move.split() if s.isdigit()]
    for i in range(x[0]):
        cont[x[2]-1].insert(0, cont[x[1]-1][0])
        cont[x[1]-1].pop(0)
print (prepare_result(cont))
"""
#task 2
print (cont2)
for m in moves:
    y = [int(t) for t in m.split() if t.isdigit()]
    for k in range(y[0],0,-1):
        cont2[y[2]-1].insert(0, cont2[y[1]-1][k-1])
    for k in range(y[0]):
        cont2[y[1]-1].pop(0)
print (prepare_result(cont2))