from typing import List

def merge_sort(nums: List[int], l: int, r: int) -> None:
    if l == r:  return
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and nums[i] <= nums[j]):
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    nums[l:r+1] = tmp


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    merge_sort(nums, 0, n - 1)
    for num in nums:
        print(num, end=' ')


if __name__ == "__main__":
    main()
