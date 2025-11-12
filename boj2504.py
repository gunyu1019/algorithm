import sys


if __name__ == '__main__':
    letter = sys.stdin.readline().strip()
    letter += " "
    small_stack = 0
    big_stack = 0
    depth = 0

    ts = 0
    s = [0 for _ in range(31)]

    for i, k in enumerate(letter[:-1]):
        pre_k = letter[i-1]

        if k == "(":
            small_stack += 1
        elif k == "[":
            big_stack += 1
        elif k == ")":
            small_stack -= 1
            if pre_k == "(":
                s[small_stack + big_stack] += 2
            else:  # ], )
                s[small_stack + big_stack] += s[small_stack + big_stack + 1] * 2
                s[small_stack + big_stack + 1] = 0
        elif k == "]":
            big_stack -= 1
            if pre_k == "[":
                s[small_stack + big_stack] += 3
            else:  # ], )
                s[small_stack + big_stack] += s[small_stack + big_stack + 1] * 3
                s[small_stack + big_stack + 1] = 0

        # print(k, small_stack, big_stack, ts, s)
        if small_stack < 0 or big_stack < 0:
            print(0)
            sys.exit(0)

    if small_stack > 0 or big_stack > 0:
        print(0)
        sys.exit(0)
    print(s[0])
