N = int(input())

Name = []
Number = []

for i in range(N):
    name, number = input().split()
    number = int(number)
    Number.append(number)
    Name.append(name)

Name.sort()
winner = sum(Number) % N

print(Name[winner])