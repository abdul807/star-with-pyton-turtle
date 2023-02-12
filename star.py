import turtle



my_tut = turtle.Turtle()
my_tut.speed(0)
turtle.delay(25)


for i in range(250):
    my_tut.forward(i*4)
    my_tut.right(144)

my_tut.hideturtle()
turtle.done()