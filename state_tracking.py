print("Printing current and previous number sum in a range(10)")
prev_no = 0

for i in range(10):
    sum = prev_no + i
    print("Current number:", i, "Previous number:", prev_no, "Sum:", sum)
    prev_no = i
    