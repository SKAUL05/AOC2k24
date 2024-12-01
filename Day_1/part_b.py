import sys

read = sys.stdin.read
f = open("input.txt")

inp = list(f.read().split("\n"))
print(inp)

x = []
y = []
for i in inp:
    x.append(int(i.split(" ")[0]))
    y.append(int(i.split(" ")[3]))
print(x)
print(y)

ans = 0
for i in x:
    ans += (y.count(i) * i)
print(ans)


