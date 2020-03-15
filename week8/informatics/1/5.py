a = input()
b = input()
c = int(a) * int(b)
if c < 0:
    if c > (-109):
        print(109 + c)
    elif c < (-109):
        print(109 + (c % (-109))) 
elif c > 0:
    if c > 109:
        print(c % 109)
    elif c < 109: 
        print(c)
elif c == 0 or c == 109:
    print("0")
