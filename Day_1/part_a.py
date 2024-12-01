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
x.sort()
y.sort()
sums = 0
for i in range(len(x)):
    sums += abs(x[i]-y[i])
print(sums)