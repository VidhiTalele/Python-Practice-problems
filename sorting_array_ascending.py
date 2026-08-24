arr = [17,18,5,4,6,1]
n = len(arr)
temp = 0

for i in range(n):
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)