n = int(input())
list = [int(x) for x in input().split(maxsplit = n)]
cnt = 0
for i in range(n - 1):
    if list[i]<0 and list[i+1] < 0 or list[i]>0 and list[i+1]>0:
        cnt += 1

if cnt == 0:
    print("NO")
else:
    print("YES")