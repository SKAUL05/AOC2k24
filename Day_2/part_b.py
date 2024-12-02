import sys
from part_a import check

read = sys.stdin.read
f = open("input.txt")

inp = list(f.read().split("\n"))

x = []
for i in inp:
    i = i.split(" ")
    i = list(map(int, i))
    x.append(i)

print(x)


def dmp_check(report):
    if check(report):
        return True
    for loop in range(len(report)):
        modified = report[:loop] + report[loop + 1 :]
        if check(modified):
            return True

    return False


cnt = 0
for rep in x:
    if dmp_check(rep):
        cnt += 1
print(cnt)
