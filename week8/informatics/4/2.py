n = int(input())
list = [int(x) for x in input().split()]
for i in range(0, n):
    if list[i] % 2 == 0:
        print(list[i], end = " ")