import math

N = int(input())
array = []

payments = 0

array.append(N)

max_array = max(array)

while max_array != 1:
    row = math.floor(max_array / 2)
    high = math.ceil(max_array / 2)
    payments = payments + max_array
    array.append(high)
    array.append(row)
    print(array)
    array.pop(0)
    max_array = max(array)

print(payments)
