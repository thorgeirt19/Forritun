n = int(input("Enter the length of the sequence: ")) # Do not change this line
last = 0
mid = 1
first = 0
sum1 = 0
for i in range(0,n):
    sum1 = first + mid + last
    last = mid
    mid = first
    first = sum1
    print(sum1)