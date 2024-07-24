def add_high_precision(s1: str, s2: str) -> str:
    def split_into_digits(s, base_size=9):
        length = len(s)
        return [int(s[max(0, length - i - base_size):length - i]) for i in range(0, length, base_size)]
        
    BASE = 1000000000
    num1 = split_into_digits(s1, 9)
    num2 = split_into_digits(s2, 9)

    carry = 0
    result = []
    max_len = max(len(num1), len(num2))
    
    for i in range(max_len):
        val1 = num1[i] if i < len(num1) else 0
        val2 = num2[i] if i < len(num2) else 0
        sum_val = val1 + val2 + carry
        result.append(sum_val % BASE)
        carry = sum_val // BASE
    
    if carry:
        result.append(carry)

    result_str = ""
    for i, num in enumerate(result):
        if i == len(result) - 1:
            result_str = str(num) + result_str
        else:
            result_str = f"{num:09d}" + result_str
    
    return result_str

def main():
    s1 = input()
    s2 = input()
    print(add_high_precision(s1, s2))


if __name__ == "__main__":
    main()
