#!/use/bin/python3
def magic_calculation(a, b):
    num = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                num += a ** b / i
        except BaseException:
            num = b + a
            break
    return num
