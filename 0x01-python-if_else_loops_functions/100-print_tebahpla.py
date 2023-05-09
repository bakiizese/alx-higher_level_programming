#!/usr/bin/python3
j = 0
for i in range(90, 64, -1):
    j = 32 if j == 0 else 0
    print(chr(i + j), end='')
