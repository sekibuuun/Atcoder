import numpy as np

line = input()

# 最初の行を解析して操作の数を取得
num_operations = int(line)

array = []

answer = []

# 残りの行を解析
for i in range(1, num_operations + 1):
    operation, parameter = map(int, input().split())
    if operation == 1:
        array = np.append(array, parameter)
    elif operation == 2:
        answer.append(int(array[-parameter]))

print(*answer, sep='\n')
