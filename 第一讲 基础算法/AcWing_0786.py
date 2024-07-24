from typing import List
import random

def find_kth(q: List[int], l: int, r: int, k: int) -> int:
    if l == r:  return q[l]

    pivot_index = random.randint(l, r)
    pivot = q[pivot_index]

    i, j = l, r
    while i <= j:
        while q[i] < pivot:
            i += 1
        while q[j] > pivot:
            j -= 1
        if i <= j:
            q[i], q[j] = q[j], q[i]
            i += 1
            j -= 1

    left_part_size = j - l + 1
    if k <= left_part_size:
        return find_kth(q, l, j, k)
    else:
        return find_kth(q, j + 1, r, k - left_part_size)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(find_kth(nums, 0, n - 1, k))
