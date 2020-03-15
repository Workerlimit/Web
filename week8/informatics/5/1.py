def minimum(a,b,c,d):
    print(min(a, min(b, min(c,d))))
a, b, c, d = input().split()
minimum(a,b,c,d)