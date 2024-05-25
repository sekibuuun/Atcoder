A, B = map(int, input().split())

if A == B:
    N = -1
else:
    if A == 1:
        if B == 2:
            N = 3
        else:
            N = 2
    elif A == 2:
        if B == 1:
            N = 3
        else:
            N = 1
    else:
        if B == 1:
            N = 2
        else:
            N = 1

print(N)
