import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)


def square(len, angle):
    for i in range(4):
        my_turtle.forward(len)
        my_turtle.left(angle)


for i in range(1000):
    square(100, 90)
    my_turtle.left(11)
