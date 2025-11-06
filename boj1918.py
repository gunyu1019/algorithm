import sys


if __name__ == '__main__':
    msg = sys.stdin.readline().rstrip()
    expr = []
    num = []

    for i in msg:
        if i == '(':
            expr.append(i)
        elif i == ')':
            while len(expr) > 0 and expr[-1] != '(':
                while len(num) > 0:
                    sys.stdout.write(num.pop(0))
                sys.stdout.write(expr.pop())
            expr.pop()
        elif i == '*' or i == '/':
            while len(expr) > 0 and (expr[-1] == '*' or expr[-1] == '/'):
                while len(num) > 0:
                    sys.stdout.write(num.pop(0))
                sys.stdout.write(expr.pop())
            expr.append(i)
        elif i == '+' or i == '-':
            while len(expr) > 0 and expr[-1] != '(':
                while len(num) > 0:
                    sys.stdout.write(num.pop(0))
                sys.stdout.write(expr.pop())
            expr.append(i)
        else:
            num.append(i)

    while len(num) > 0:
        sys.stdout.write(num.pop(0))
    while len(expr) > 0:
        sys.stdout.write(expr.pop())
