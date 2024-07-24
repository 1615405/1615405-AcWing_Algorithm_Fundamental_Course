def big_number_division(A, B):
    BASE = 10**9
    split_number = lambda num: [int(num[max(i-9, 0):i]) for i in range(len(num), 0, -9)][::-1]
    a_parts = split_number(A)
    b = int(B)
    remainder = 0
    result = []
    for part in a_parts:
        current = remainder * BASE + part
        result.append(current // b)
        remainder = current % b
    if result:
        final_result = [str(result[0])]
        final_result.extend(f"{num:09d}" for num in result[1:])
        quotient = ''.join(final_result).lstrip('0') or '0'
    else:
        quotient = '0'
    return quotient, remainder


A = input()
B = input()

quotient, remainder = big_number_division(A, B)
print(quotient)
print(remainder)
