from turtle import left, right, shape, forward, exitonclick, penup, pendown

shape('turtle')

for i in range(20):

    forward(i * 2)
    penup()
    forward(5)
    pendown()
    
exitonclick()    

 