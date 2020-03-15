n = int(input())
list = [int(x) for x in input().split(maxsplit=n)]
cnt = 0
for i in range(n):
    if list[i] >= 0:
        cnt += 1
print(cnt)