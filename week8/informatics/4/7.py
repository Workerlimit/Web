n = int(input())
list = [int(x) for x in input().split(maxsplit=n)]
list.reverse()
for i in range(n):
    print(list[i], end = " ")