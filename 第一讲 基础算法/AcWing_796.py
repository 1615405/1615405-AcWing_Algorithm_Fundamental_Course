def main():
    n, m, q = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    s = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            # 根据前缀和公式，加上当前值，并加上左侧和上方的值，减去重叠区域的值
            s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + value
    
    # 处理每一个查询
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        # 根据前缀和矩阵获取查询区域的和
        result = s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]
        print(result)

if __name__ == "__main__":
    main()
