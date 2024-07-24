from typing import List
import random

def find_kth(q: List[int], l: int, r: int, k: int) -> int:
    if l == r:  return q[l]
    pivot_index = random.randint(l, r)
    pivot = q[pivot_index]
    i, j = l - 1, r + 1
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
    left_part_size = j - l + 1
    if k <= left_part_size:
        return find_kth(q, l, j, k)
    else:
        return find_kth(q, j + 1, r, k - left_part_size)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(find_kth(nums, 0, n - 1, k))
