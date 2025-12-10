import time
import re
import scipy

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split('\n')
if len(inp[-1]) == 0:
    inp.pop()

machines = []
buttons = []
joltages = []

for line in inp:
    mach = re.findall(r'\[([^\]]*)\]', line)
    machines.append(mach[0])

    buts = re.findall(r'\(([^\(]*)\)', line)
    buts = [[int(x) for x in but.split(',')] for but in buts]
    buttons.append(buts)

    jolts = re.findall(r'\{([^\{]*)\}', line)
    jolts = [int(x) for x in jolts[0].split(',')]
    joltages.append(jolts)



def find_xors(target, nums):
    ans = []
    n = len(nums)
    least = n + 1

    for i in range(2**n):
        # Each i is one subset
        xor = 0
        subset = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                xor ^= nums[j]
                subset.append(j)
            
        if xor == target and len(subset) < least:
            least = len(subset)
            ans = subset
    return ans

def part1():
    nbuts = []
    for i, buts in enumerate(buttons):
        nbut = [sum([2**( len(machines[i]) - x - 1) for x in but]) for but in buts]
        nbuts.append(nbut)

    ans = 0
    for i, mach in enumerate(machines):
        target = 0
        for j, ch in enumerate(mach[-1::-1]):
            if ch == '#':
                target += 2**j
        ans += len(find_xors(target, nbuts[i]))
    return ans


def part2():
    ans = 0
    for i, jolts in enumerate(joltages):
        buts = buttons[i]
        
        A = [[0 for i_ in range(len(buts))] for j in range(len(jolts))]
        for j, but in enumerate(buts):
            for light in but:
                A[light][j] = 1

        c = [1 for i_ in range(len(buts))]
        res = scipy.optimize.linprog(c, A_eq=A, b_eq=jolts, integrality=1)

        if not res.success:
            print("Couldn't find optimal solution")
            return -1

        ans += sum(res.x)
    return ans

start = time.time()

print(part1())
# print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")