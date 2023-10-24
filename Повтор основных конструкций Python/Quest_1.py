
n = int(input())

field = [[min(i, j, n-i-1, n-j-1) + 1 for j in range(n)] for i in range(n)]

for row in field:
    print(*row)