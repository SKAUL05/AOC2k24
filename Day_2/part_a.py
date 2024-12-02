import sys

read = sys.stdin.read
f = open("input.txt")

inp = list(f.read().split("\n"))

x = []
for i in inp:
    i = i.split(" ")
    i = list(map(int, i))
    x.append(i)

print(x)


def check(report):
    inc = all(report[loop] < report[loop + 1] for loop in range(len(report) - 1))
    dec = all(report[loop] > report[loop + 1] for loop in range(len(report) - 1))

    valid = all(1 <= abs(report[loop] - report[loop + 1]) <= 3 for loop in range(len(report) - 1))

    return (inc or dec) and valid


cnt = 0
for rep in x:
    if check(rep):
        cnt += 1
print(cnt)
