arr=[1,2,3,4]
a=0
for i in range(len(arr) - 1, len(arr) // 2 - 1, -1):
    arr[i], arr[a] = arr[a], arr[i]
    a += 1
print(arr)
