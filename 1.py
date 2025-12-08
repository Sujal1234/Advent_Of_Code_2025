import time

with open("inp", 'r') as f:
    inp = f.read()
inp = inp.split('\n')
inp.pop()

def part1():
    dial = 50
    ans = 0

    for line in inp:
        num = int(line[1:])

        if(line[0] == 'L'):
            num *= -1
        dial = (dial + num) % 100

        if dial == 0:
            ans += 1
    return ans


def part2():
    dial = 50
    ans = 0

    for line in inp:
        was0 = (dial == 0)

        num = int(line[1:])
        ans += num // 100
        num %= 100
        
        if(line[0] == 'L'):
            if(num >= dial and dial != 0):
                ans += 1
            num *= -1
        else:
            if(num >= 100 - dial and dial != 0):
                ans += 1

        dial += num
        dial %= 100
    return ans

start = time.time()

print(part1())
# print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")