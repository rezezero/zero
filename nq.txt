n = int(input("Enter N: "))
b = [[0]*n for _ in range(n)]

def safe(row, col):
    if any(b[i][col] for i in range(row)):
        return False

    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if b[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row-1, col+1
    while i >= 0 and j < n:
        if b[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve(row=0):
    if row == n:
        print(b)
        return

    for col in range(n):
        if safe(row, col):
            b[row][col] = 1
            solve(row+1)
            b[row][col] = 0

solve()