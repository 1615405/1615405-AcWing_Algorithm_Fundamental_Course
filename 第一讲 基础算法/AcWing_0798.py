def main():
    n, m, q = map(int, input().split())

    matrix = []
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    def insert(r1: int, c1: int, r2: int, c2: int, val: int) -> None:
        diff[r1][c1] += val
        diff[r2 + 1][c1] -= val
        diff[r1][c2 + 1] -= val
        diff[r2 + 1][c2 + 1] += val

    for i in range(n):
        for j in range(m):
            x = matrix[i][j]
            insert(i, j, i, j, x)

    for _ in range(q):
        r1, c1, r2, c2, c = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        insert(r1, c1, r2, c2, c)

    for i in range(n):
        for j in range(m):
            if i > 0:
                diff[i][j] += diff[i-1][j]
            if j > 0:
                diff[i][j] += diff[i][j-1]
            if i > 0 and j > 0:
                diff[i][j] -= diff[i-1][j-1]

    for i in range(n):
        for j in range(m):
            print(diff[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()
