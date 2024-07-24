from typing import List

def quick_sort(q: List[int], l: int, r: int) -> None:
    if l >= r:  return
    i, j = l, r
    pivot = q[(l + r) // 2]
    while i <= j:
        while q[i] < pivot:
            i += 1
        while q[j] > pivot:
            j -= 1
        if i <= j:
            q[i], q[j] = q[j], q[i]
            i += 1
            j -= 1
    quick_sort(q, l, j)
    quick_sort(q, i, r)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums) - 1)
    
    for x in nums:
        print(x, end=' ')
