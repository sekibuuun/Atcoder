String = input()

first = String[0]
remaining = String[1:]

if (first.isupper() == True):
    if (remaining.islower() == True or len(remaining) == 0):
        print('Yes')
    else:
        print('No')
else:
    print('No')
