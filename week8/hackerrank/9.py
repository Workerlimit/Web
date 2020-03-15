n = int(input())
info = []
for i in range(2*n):
    info.append(input().split())

marks = {}
for j in range(0, len(info), 2):
    marks[info[j][0]] = float(info[j+1][0])
res = []
num = sorted(set(marks.values()))[1]
for k in marks.keys():
    if marks[k] == num:
        res.append(k)
for l in sorted(res):
    print(l)
