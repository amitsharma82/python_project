# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint  # |  \
x = randint(-100, 100)  # |   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)  # |     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)  # |    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)  # |  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /

# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x < 0 and y < 0:
    print(f"both negativ x = {x} and y = {y}")

elif x > 0 and y > 0:
    print(f"both posativ x = {x} and y = {y}")

elif x > 0 and y < 0:
    print(f"x {x} is positive and y {y} is negative")

else:
    print(f" {y} y is positive and {x} x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
