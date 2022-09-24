#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last = number % 10
if number < 0:
    last = number % -10
else:
    last = number % 10
print("Last Digit of {} is {} and is ".format(number, last), end="")
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0".format(number, last))
