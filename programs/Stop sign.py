import turtle
turtle.title("Stop sign")
turtle.penup()
turtle.hideturtle()
turtle.goto(-80,150)
turtle.color("black","red")
turtle.begin_fill()
turtle.pendown()
for i in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()
turtle.penup()
turtle.color("white")
turtle.goto(-30,5)
turtle.write("STOP",align="center",font=("algerian",40,"bold"))
turtle.done()