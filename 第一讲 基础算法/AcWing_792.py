def main():
    def split_into_digits(s, base_size=9):
        length = len(s)
        return [int(s[max(0, length - i - base_size):length - i]) for i in range(0, length, base_size)]

    def subtract_high_precision(s1: str, s2: str) -> str:
        BASE = 1000000000

        sign = 1
        num1_bigger = (len(s1) > len(s2)) or (len(s1) == len(s2) and s1 > s2)
        if not num1_bigger:
            s1, s2 = s2, s1
            sign = -1

        num1 = split_into_digits(s1, 9)
        num2 = split_into_digits(s2, 9)

        result = []
        borrow = 0

        # 执行减法操作
        for i in range(max(len(num1), len(num2))):
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0
            diff = val1 - val2 - borrow
            if diff < 0:
                diff += BASE
                borrow = 1
            else:
                borrow = 0
            result.append(diff)

        # 删除结果中的前导零
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        if result == [0]:
            return '0'
        result_str = ''.join(map(lambda x: f"{x:09d}", reversed(result))).lstrip('0')
        if sign == -1:
            result_str = '-' + result_str
        return result_str

    num1 = input()
    num2 = input()

    print(subtract_high_precision(num1, num2))


if __name__ == "__main__":
    main()
