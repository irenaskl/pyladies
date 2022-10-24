from turtle import left, right, shape, forward, exitonclick, penup, pendown, back


shape('turtle')
penup()
back(300)
pendown()

for n in (5,6,7,8,95):
    uhel = (180-(180 * (1 - 2/n)))
    strana = (300 / n)
    for i in range(n):
        forward(strana)
        left(uhel)
    penup()
    forward(150)
    pendown()

exitonclick()