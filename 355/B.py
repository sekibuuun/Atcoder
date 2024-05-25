N, M = map(int, input().split())

for i in range(N):
  arr1 = list(map(int, input().split()))
  break

for i in range(N):
  arr2 = list(map(int, input().split()))
  break

arr = arr1 + arr2

arr.sort()

count = 0

for i in range(len(arr) - 1):
  if arr[i] in arr1 and arr[i+1] in arr1:
    count = count + 1
    print("Yes")
    break
  else:
    continue

if count == 0:
  print("No")