import turtle
t1=turtle.Turtle()
t1.up()
t1.goto(0,-100)
t1.down()

for t in range(1,50):
    t1.circle(t)
    t1.left(90)
    t1.fd(2)
    t1.rt(90)
