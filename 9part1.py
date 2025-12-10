import time
from functools import *
from itertools import *

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

tiles = [line.split(',') for line in inp]
tiles = [(int(a[0]), int(a[1])) for a in tiles]


xs = [x for x, y in tiles]
ys = [y for x, y in tiles]
minx, miny, maxx, maxy = min(xs), min(ys), max(xs), max(ys)

tiles = [(x - minx + 1, y - miny + 1) for x, y in tiles]
maxx -= minx
maxy -= miny

areas = []
def part1():
    global areas
    ans = -1
    for i, t1 in enumerate(tiles):
        for j, t2 in enumerate(tiles):
            if j <= i:
                continue

            area = (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
            areas.append([area, t1, t2])
            ans = max(ans, area)
    return ans


def part2():
    pass

start = time.time()

print(part1())
# print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")