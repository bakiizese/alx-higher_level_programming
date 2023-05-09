#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lm = abs(number) % 10
if number < 0:
    lm = -lm
if lm > 5:
    print(f"Last digit of {number} is {lm} and is greater than 5")
elif lm == 0:
    print("Last digit of {} is {} and is 0".format(number, lm))
else:
    print(f"Last digit of {number} is {lm} and is less than 6 and not 0")
