n = int(input("Enter the range of numbers: "))
temp1 = 0
temp2 = 0
for i in range(n):
    nums = int(input("Enter the number:"))
    if nums > temp1:
        temp2 = temp1
        temp1 = nums 
    elif nums > temp2:
        temp2 = nums
print("The second largest number is:", temp2)