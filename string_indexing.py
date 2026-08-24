#Solution 1
string = input("Enter a string:")
print(string[::2])

#or


#Solution 2
string = input("Enter a string:")
n = len(string)

for i in range(0,n,2):
    print(string[i])

#or

#Solution 3
string = input("Enter a string:")
n = len(string)
for i in range(n):
    if i%2 == 0:
        print(string[i])