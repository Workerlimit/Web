n = int(input())
list = [int(x) for x in input().split()]
cnt = 0
for i in range(n - 1):
    if list[i + 1] > list[i]:
        cnt += 1
print(cnt)