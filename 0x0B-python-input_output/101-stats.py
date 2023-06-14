#!/usr/bin/python3
'''print stats'''


def print_stats(size, status_codes):
    '''accumulated matix'''
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    s_code = {}
    v_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                p_stats(size, s_code)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in v_code:
                    if s_code.get(line[-2], -1) == -1:
                        s_code[line[-2]] = 1
                    else:
                        s_code[line[-2]] += 1
            except IndexError:
                pass

        p_stats(size, s_code)

    except KeyboardInterrupt:
        p_stats(size, s_code)
        raise
