H = int(input())

plant = 0
i = 0

while H >= plant:
    plant = plant + 2 ** i
    i += 1

print(i)
