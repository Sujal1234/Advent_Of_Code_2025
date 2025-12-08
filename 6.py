import time
from functools import *

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

ops = inp[-1]
ops = ops.split()
inp.pop()

def part1():
    global inp
    inp = [line.split() for line in inp]

    inp = [[int(x) for x in line] for line in inp]

    # print(inp)
    # print(ops)

    ans = 0
    probs = [[line[i] for line in inp] for i in range(len(inp[0]))]
    # print(f"probs final = {probs}")
    for i, op in enumerate(ops):
        if op == '+':
            num = sum(probs[i])
        else:
            num = reduce(lambda x, y: x*y, probs[i])
        ans += num
    return ans

def getNum(col):
    strl = [d for d in col if d != ' ']
    numstr = ''.join(strl)
    # print(f"num string = {numstr}")
    return int(numstr)

def part2():
    global inp

    probs = [[]]
    
    for i in range(len(inp[0])):
        col = [line[i] for line in inp]
        if all(ch == ' ' for ch in col):
            probs.append([])
            continue

        # print(f"col = {col}")
        # print(f"num = {getNum(col)}")
        probs[-1].append(getNum(col))

    ans = 0
    for i, prob in enumerate(probs):
        if ops[i] == '+':
            num = sum(prob)
        else:
            num = reduce(lambda x, y: x*y, prob)
        ans += num
    return ans

start = time.time()

# print(part1())
print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")