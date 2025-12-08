import time

def sumAB(a, b):
    return b*(b+1)/2 - (a-1)*a/2

with open("inp", 'r') as f:
    inp = f.read()

inp = inp.split(',')
inp = [r.split('-') for r in inp]

def part1():
    ans = 0
    for (l ,r) in inp:
        if len(l) % 2 == 0:
            a = l[: len(l)//2]
            if(int(a+a) < int(l)):
                a = int(a) + 1
                
        elif len(r) % 2 == 0:
            a = '1' + '0'*(len(r)//2 - 1)
        else:
            continue
        
        ID = int(f"{a}{a}")
        l, r = int(l), int(r)
        a = int(a)

        while(ID >= l and ID <= r):
            ans += ID
            a += 1
            ID = int(f"{a}{a}")
    return ans

def isInvalid(a):
    strA = str(a)
    for i in range(1, len(strA)):
        if len(strA) % i != 0:
            continue
        part = strA[ : i]
        if part * (len(strA)//i) == strA:
            return True
    return False

def part2():
    ans = 0
    for (l, r) in inp:
        intL = int(l)
        intR = int(r)
        # print(f"l = {l}, r = {r}")
        for i in range(intL, intR + 1):
            if isInvalid(i):
                # print(i, end = ' ')
                ans += i
    return ans

start = time.time()

print(part1())
# print(part2())

end = time.time()
print(f"Took {(end - start) * 1000} ms")