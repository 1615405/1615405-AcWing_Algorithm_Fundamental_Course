import itertools

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    # 初始化差分数组
    diff = [0] * (n + 2)
    for i in range(n):
        if i == 0:
            diff[i] = nums[i]
        else:
            diff[i] = nums[i] - nums[i - 1]

    def insert(from_: int, to: int, val: int) -> None:
        # 在差分数组中进行区间操作
        diff[from_] += val
        diff[to + 1] -= val

    for _ in range(m):
        l, r, val = map(int, input().split())
        insert(l - 1, r - 1, val)

    result = list(itertools.accumulate(diff[:n]))
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
