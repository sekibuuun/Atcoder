import itertools

N = int(input())

array1 = []
array2 = []

for i in range(N):
    attack, cost = input().split()
    array1.append(i + 1)
    array1.append(int(attack))
    array1.append(int(cost))
    array2.append(array1)
    array1 = []
    i += 1

delete_list = []

for pair in itertools.combinations(array2, 2):
    pair_list = list(pair)
    if pair_list[0][1] < pair_list[1][1] and pair_list[0][2] > pair_list[1][2]:
        delete_list.append(pair_list[0])

unique_arr = [list(sub_arr) for sub_arr in set(tuple(sub_arr) for sub_arr in delete_list)]


for i in range(len(unique_arr)):
    array2.remove(unique_arr[i])

print(len(array2))

for i in range(len(array2)):
    if i != len(array2) - 1:
        print(array2[i][0], end=' ')
    else:
        print(array2[i][0], end='')