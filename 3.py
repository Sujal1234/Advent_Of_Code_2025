import time

with open("inp", 'r') as f:
    inp = f.read()
inp = inp.split('\n')

if len(inp[-1]) == 0:
    inp.pop()

inp = [list(line) for line in inp]
inp = [[int(n) for n in bank] for bank in inp]

def solve(N):
    # N digits
    ans = 0
    for bank in inp:
        maxind = 0
        num = 0
        for k in range(N-1, -1, -1):
            for i in range(maxind, len(bank) - k):
                if bank[i] > bank[maxind]:
                    maxind = i
            num = num * 10 + bank[maxind]
            maxind += 1
            
        ans += num
    return ans

def part1():
    return solve(2)

def part2():
    return solve(12)

start = time.time()

# print(part1())
print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")
