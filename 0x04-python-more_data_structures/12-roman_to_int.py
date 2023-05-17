#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    n = 0
    tk = 0
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    for i in reversed(roman_string):
        n = roms[i]
        tk += n if tk < n * 5 else -n
    return tk
