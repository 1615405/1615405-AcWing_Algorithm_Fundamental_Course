from typing import List

def min_interval_groups(intervals):
    intervals.sort()
    import heapq
    heap = []
    for interval in intervals:
        if heap and heap[0] < interval[0]:
            heapq.heapreplace(heap, interval[1])
        else:
            heapq.heappush(heap, interval[1])
    return len(heap)


if __name__ == "__main__":
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    
    ans = min_interval_groups(intervals)
    print(ans)
