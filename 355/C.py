import numpy as np

def check_any_row_equal(array):
    # 各行の値がすべて同じかどうかを確認
    rows_equal = np.all(array == array[:, [0]], axis=1)
    # 1つでもTrueがあればTrueを返す
    return np.any(rows_equal)

def check_any_column_equal(array):
    column_equal = np.all(array == array[0, :], axis=0)
    return np.any(column_equal)

def check_diagonals_equal(array):
    # 主対角線のチェック
    main_diagonal_equal = np.all(array.diagonal() == array[0, 0])
    # 副対角線のチェック
    anti_diagonal_equal = np.all(np.fliplr(array).diagonal() == array[0, -1])

    return main_diagonal_equal or anti_diagonal_equal

def find_indices_of_value(array, value):
    # np.whereを使用して条件に合う要素のインデックスを取得
    result = np.where(array == value)
    # インデックスをリストに変換
    indices = list(zip(result[0], result[1]))
    return indices

# # N = 3 for a 3x3 2D array
N, T = map(int, input().split())
array_2d = np.arange(1, N*N+1).reshape(N, N)

for i in range(T):
  output = list(map(int, input().split()))
  break


for i in range(len(output)):
  indices = find_indices_of_value(array_2d, output[i])
  row = indices[0][0]
  column = indices[0][1]
  array_2d[row][column] = 0
  if check_any_column_equal(array_2d) or check_any_row_equal(array_2d) or check_diagonals_equal(array_2d):
    print(i+1)
    break

if i == T-1:
  print(-1)