import time
from functools import *
from itertools import *

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

grid = [list(line) for line in inp]

def part1():
    global grid
    beams = set()
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            beams.add(i)

    ans = 0

    beams2 = set(beams)
    for row in range(len(grid) - 1):
        for col in beams:
            if grid[row+1][col] == '^':
                ans += 1

                if col - 1 >= 0:
                    beams2.add(col - 1)
                if col + 1 < len(grid[0]):
                    beams2.add(col + 1)
                beams2.remove(col)

        beams = set(beams2)
    return ans

def part2():
    global grid
    dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            dp[0][i] = 1
            break

    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if dp[i][j] == 0:
                continue

            if grid[i+1][j] == '^':
                if j - 1 >= 0:
                    dp[i+1][j-1] += dp[i][j]
                if j + 1 < len(grid[0]):
                    dp[i+1][j+1] += dp[i][j]
            else:
                dp[i+1][j] += dp[i][j]

    return sum(dp[-1])


start = time.time()

# print(part1())
print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")