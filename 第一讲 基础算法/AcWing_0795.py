from typing import List

def foo(prefix_sum: List[int], l: int, r: int) -> int:
    return prefix_sum[r + 1] - prefix_sum[l]
    
if __name__ == "__main__":
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))
    
    prefix_sum = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    for _ in range(t):
        l, r = map(int, input().split())
        print(foo(prefix_sum, l - 1, r - 1))
