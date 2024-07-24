def main():
    n = int(input())
    nums = list(map(int, input().split()))

    def merge_sort(l: int, r: int) -> None:
        if l >= r:  return

        mid = (l + r) // 2  # 计算中点
        merge_sort(l, mid)  # 递归排序左半部分
        merge_sort(mid + 1, r)  # 递归排序右半部分

        tmp = []
        i, j = l, mid + 1  # 初始化两个指针，分别指向两个部分的起始位置
        for k in range(l, r + 1):  # 从l到r遍历区间
            # 如果右半部分已经全部加入临时数组，或者左半部分的当前元素小于等于右半部分的当前元素
            if j > r or (i <= mid and nums[i] <= nums[j]):
                tmp.append(nums[i])
                i += 1  # 移动左半部分的指针
            else:
                tmp.append(nums[j])
                j += 1  # 移动右半部分的指针

        nums[l:r+1] = tmp

    merge_sort(0, n - 1)
    for num in nums:
        print(num, end=' ')


if __name__ == "__main__":
    main()
