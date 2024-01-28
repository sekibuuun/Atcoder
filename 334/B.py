A, M, L, R = map(int, input().split())

def count_trees(A, M, L, R):
    left_trees = max(0, (A - L + M - 1) // M)
    right_trees = max(0, (R - A - M + M - 1) // M)
    print(left_trees, right_trees)
    return left_trees + right_trees + 1

tree = count_trees(A, M, L, R)
print(tree)

if L == R:
    print(1 if A == L else 0)
