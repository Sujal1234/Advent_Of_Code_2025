import time

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

brk = 0
for i in range(len(inp)):
    if len(inp[i]) == 0:
        brk = i
        break

fresh = inp[:brk]
ids = inp[brk+1:]

for i, string in enumerate(fresh):
    fresh[i] = (int(string.split('-')[0]), int(string.split('-')[1]))

ids = [int(i) for i in ids]

def isFresh(ID):
    for l, r in fresh:
        if l <= ID <= r:
            return True
    return False

def part1():
    return len([i for i in ids if isFresh(i)])

def part2():
    fresh.sort()
    l = 0
    r = -1
    ans = 0
    for i, j in fresh:
        if i > r:
            num = j - i + 1
            r = j
        else:
            if j <= r:
                continue
            num = max(0, j - r)
            r = j
        ans += num
    return ans


start = time.time()

# print(part1())
print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")