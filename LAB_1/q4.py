rows = int(input("Rows: "))
cols = int(input("Columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    matrix.append(list(map(int, input().split())))

print("Transpose:")

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()