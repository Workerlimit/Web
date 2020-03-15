n = int(input())
list = [int(x) for x in input().split(maxsplit=n)]
cnt = 0

for i in range(1, n - 1):
    if list[i - 1] < list[i] and list[i] > list[i + 1]:
        cnt += 1
print(cnt)