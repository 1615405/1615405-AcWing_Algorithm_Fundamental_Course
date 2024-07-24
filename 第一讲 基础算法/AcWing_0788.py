from typing import List

def inversion_pair(nums: List[int], l: int, r: int) -> int:
    if l == r:  return 0
    mid = (l + r) // 2
    ans = inversion_pair(nums, l, mid) + inversion_pair(nums, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and nums[i] <= nums[j]):
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
            ans += mid - i + 1
    nums[l:r+1] = tmp
    return ans
        

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(inversion_pair(nums, 0, n - 1))


if __name__ == "__main__":
    main()
