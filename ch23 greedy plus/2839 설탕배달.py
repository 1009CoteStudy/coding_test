n = int(input())

if n%5 == 0:
    print(n//5)
elif n%5 == 1:
    if n>5:
        print(n//5-1+2)
    else:
        print(-1)
elif n%5 == 2:
    if n>11:
        print(n//5-2+4)
    else:
        print(-1)
elif n%5 == 3:
    if n>2:
        print(n//5+1)
    else:
        print(-1)
elif n%5 == 4:
    if n>8:
        print(n//5-1+3)
    else:
        print(-1)