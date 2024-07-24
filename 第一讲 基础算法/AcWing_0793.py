def large_multiplication(A: str, B: str) -> str:
    if B == '0' or A == '0':
        return '0'
    BASE = 10**9
    a_list = [int(A[max(i-9, 0):i]) for i in range(len(A), 0, -9)]
    b_list = [int(B[max(i-9, 0):i]) for i in range(len(B), 0, -9)]
    result = [0] * (len(a_list) + len(b_list))
    # 执行多位乘法
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            result[i + j] += a_list[i] * b_list[j]
            result[i + j + 1] += result[i + j] // BASE
            result[i + j] %= BASE
    for i in range(len(result) - 1):
        result[i + 1] += result[i] // BASE
        result[i] %= BASE
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(str(x).zfill(9) for x in reversed(result)).lstrip('0')


if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(large_multiplication(A, B))
