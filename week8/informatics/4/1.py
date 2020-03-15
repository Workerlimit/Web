n = int(input())
list = [int(x) for x in input().split()]

for i in range(0, n, 2):
    print(list[i], end = " ")