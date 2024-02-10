A, B, D = map(int, input().split())

N = 1

answer = []

a_n = A + (N - 1) * D

if A == B:
    print(A, end=' ')
else:
    while a_n < B:
        a_n = A + (N - 1) * D
        N += 1
        if a_n <= B:
            answer.append(a_n)
    for i in range(len(answer)):
        print(answer[i], end=' ')
