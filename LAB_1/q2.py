r1 = int(input("Rows of A: "))
c1 = int(input("Columns of A: "))

A = []

print("Enter Matrix A:")

for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Rows of B: "))
c2 = int(input("Columns of B: "))

B = []

print("Enter Matrix B:")

for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

if c1 != r2:
    print("Matrices cannot be multiplied")
else:
    result = []

    for i in range(r1):
        row = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)

    print("Product Matrix:")
    for row in result:
        print(row)