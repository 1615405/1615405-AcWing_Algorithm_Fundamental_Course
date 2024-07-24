from typing import List

def quick_sort(q: List[int], l: int, r: int) -> None:
    if l == r:  return
    i, j = l - 1, r + 1
    pivot = q[(l + r) // 2]
    while i < j:
        while True:
            i += 1
            if q[i] >= pivot:
                break
        while True:
            j -= 1
            if q[j] <= pivot:
                break
        if i < j:
            q[i], q[j] = q[j], q[i]
    quick_sort(q, l, j)
    quick_sort(q, j + 1, r)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums) - 1)
    
    for x in nums:
        print(x, end=' ')
