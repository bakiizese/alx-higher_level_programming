#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
if number < 0:
    l = -l
if l > 5:
    print(f"Last digit of {number} is {l} and is greater than 5")
elif l == 0:
    print("Last digit of {} is {} and is 0".format(number, l))
else:
    print(f"Last digit of {number} is {l} and is less than 6 and not 0")
