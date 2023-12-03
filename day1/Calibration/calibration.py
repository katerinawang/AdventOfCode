def first_num(s):
    num = 0
    for i, c in enumerate(s):
        if c.isdigit():
            num = int(c)
            break
    return num


def first_num_string(s):
    num = 0
    for i, c in enumerate(s):
        i += 1
        if not c.isdigit():
            if "one" in s[0:i] or "eno" in s[0:i]:
                num = 1
                break
            if "two" in s[0:i] or "owt" in s[0:i]:
                num = 2
                break
            if "three" in s[0:i] or "eerht" in s[0:i]:
                num = 3
                break
            if "four" in s[0:i] or "ruof" in s[0:i]:
                num = 4
                break
            if "five" in s[0:i] or "evif" in s[0:i]:
                num = 5
                break
            if "six" in s[0:i] or "xis" in s[0:i]:
                num = 6
                break
            if "seven" in s[0:i] or "neves" in s[0:i]:
                num = 7
                break
            if "eight" in s[0:i] or "thgie" in s[0:i]:
                num = 8
                break
            if "nine" in s[0:i] or "enin" in s[0:i]:
                num = 9
                break
        else:
            num = int(c)
            break
    return num


def main():
    num1 = 0
    num2 = 0
    f = open("string", "r")
    for ln in f:
        num1 += first_num(ln) * 10 + first_num(ln[::-1])
        num2 += first_num_string(ln) * 10 + first_num_string(ln[::-1])
    f.close()
    print(num1)
    print(num2)


if __name__ == '__main__':
    main()
