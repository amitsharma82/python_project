for number in range(1, 10, 2):
    print(f"{number}")

x = 0


# YOUR CODE GOES HERE:
for n in range(10, 21):  # remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n
        print(f"{n}")

