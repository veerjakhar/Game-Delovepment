matrix = [[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]

print(matrix)

print(len(matrix))

print(len(matrix[0]))
print(matrix[2][1])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i] [j], end = ",")
    print("\n")

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of colums: "))
matrix1 = []

for i in range(row):
    temp = []

    for j in range(col):
        x = int(input("Enter your element: "))
        temp.append(x)
    matrix1.append(temp)

for i in range(0, len(matrix1)):
    for j in range(0, len(matrix1[0])):
        print(matrix1[i] [j], end = ",")
    print("\n")
