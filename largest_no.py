# largest number without using dsa or fucntions 
n = int(input("Enter the range of numbers: "))
temp = 0 
for i in range(n):
    nums = int(input("Enter the number: "))
    if nums > temp:
        temp = nums
print("The largest number is:", temp)