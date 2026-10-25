rows = int(input("Enter the number of rows: "))

#Right Triangle
print("Right Triangle:")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#Floyd's Triangle
print("Floyd's Triangle:")
num = 1
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(num, end = " ")
        num +=1
    print()
print()

#diamond
print("Diamond: ")
if rows % 2 == 1:
    mid = (rows+1)//2
else:
    mid = rows // 2

for i in range(1, rows +1):
    if i <= mid: 
        spaces = mid - i
        cols = 2 * i - 1
    else:
        if rows%2 == 1:
            m_row = 2*mid-i
        else:
            m_row = rows - i +1
        spaces = mid - m_row
        cols = 2* m_row - 1
    print(" " * spaces, end="")
    for j in range(1, cols+1):
        print(j, end="")
    print()   