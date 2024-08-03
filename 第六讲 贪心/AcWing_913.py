def minimize_total_wait(times):
    """
    根据给定的处理时间列表，计算并返回按最优顺序执行时的最小总等待时间。
    """
    times.sort()
    total_waiting_time = 0
    current_wait = 0
    for time in times:
        total_waiting_time += current_wait
        current_wait += time
    return total_waiting_time


if __name__ == "__main__":
    n = int(input())
    times = list(map(int, input().split()))
    print(minimize_total_wait(times))
