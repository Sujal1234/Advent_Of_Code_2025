import time

with open("inp", 'r') as f:
    inp = f.read()

grid = inp.split('\n')
if grid[-1] == "":
    grid.pop()

grid = [list(r) for r in grid]

def isGood(r, c):
    return countAdj(r, c) < 4

def countAdj(r, c):
    num = 0

    for rr in range(r-1, r+2):
        for cc in range(c-1, c+2):
            if rr == r and cc == c:
                continue
            if rr < 0 or rr >= len(grid) or cc < 0 or cc >= len(grid[0]):
                continue
            if grid[rr][cc] == '@':
                num += 1
    return num

def part1():
    ans = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '@' and isGood(i, j):
                ans += 1
    return ans

def part2():
    ans = 0

    while True:
        numGood = 0
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == '@' and isGood(i, j):
                    numGood += 1
                    grid[i][j] = '.'

        ans += numGood
        if numGood == 0:
            break
    return ans

def part2Better():
    ans = 0
    adj = dict()

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '@':
                adj[(i, j)] = countAdj(i, j)
    
    while True:
        numGood = 0
        for (i, j), count in adj.items():
            if count < 4:
                numGood += 1
                grid[i][j] = '.'
                adj[(i, j)] = 100

                for rr in range(i-1, i+2):
                    for cc in range(j-1, j+2):
                        if rr == i and cc == j:
                            continue
                        if rr < 0 or rr >= len(grid) or cc < 0 or cc >= len(grid[0]):
                            continue
                        if grid[rr][cc] == '@':
                            adj[(rr, cc)] -= 1
        ans += numGood
        if numGood == 0:
            break
    return ans

start = time.time()

# print(part1())
# print(part2())
print(part2Better())

end = time.time()
print(f"Took {(end - start) * 1000} ms")