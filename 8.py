import time
# from functools import *
# from itertools import *

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

cords = [line.split(',') for line in inp]
cords = [[int(a) for a in line] for line in cords]

# print(cords)

class DisjointSetUnion:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1 for i in range(size)]

        self.count = size # Number of disjoint sets

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by size: Attach the smaller size tree under the higher size tree
            if self.size[root_i] < self.size[root_j]:
                self.parent[root_i] = root_j
                self.size[root_j] = self.size[root_i] + self.size[root_j]

            elif self.size[root_i] > self.size[root_j]:
                self.parent[root_j] = root_i
                self.size[root_i] = self.size[root_i] + self.size[root_j]
            else:
                # If sizes are the same, attach one to the other and increment the size
                self.parent[root_j] = root_i
                self.size[root_i] = self.size[root_i] + self.size[root_j]
            self.count -= 1
            return True
        return False

    def is_connected(self, i, j):
        return self.find(i) == self.find(j)


dsu = DisjointSetUnion(len(cords))


def calc_dist(c1, c2):
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2

dists = []
for i, c1 in enumerate(cords):
    for j in range(i+1, len(cords)):
        c2 = cords[j]
        d = calc_dist(c1, c2)
        dists.append((d, i, j))


dists.sort()

def part1():

    for i in range(1000):
        # connect 1000 closest
        dsu.union(dists[i][1], dists[i][2])

    circs = []
    vis = set()

    for i in range(len(cords)):
        par = dsu.find(i)
        if(par in vis):
            continue
        vis.add(par)

        circs.append(dsu.size[par])
    
    circs.sort()
    return circs[-1] * circs[-2] * circs[-3]


def part2():
    mult = 0
    for d, i, j in dists:
        c1 = cords[i]
        c2 = cords[j]
        mult = c1[0] * c2[0]
        dsu.union(i, j)

        if dsu.count == 1:
            break
    return mult

start = time.time()

# print(part1())
print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")