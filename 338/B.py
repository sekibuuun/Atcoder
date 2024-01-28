import collections

String = input()
counter = collections.Counter(String).most_common()

array = []

max = counter[0][1]

if len(String) == 1:
    print(String[0])
else:
    i = 0
    while i < len(counter) and counter[i][1] == max:
        array.append(counter[i][0])
        i += 1
    array.sort()
    print(array[0])
