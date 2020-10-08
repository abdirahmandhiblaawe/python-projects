from turtle import Turtle, Screen, Shape
screen = Screen()
screen.bgcolor("red")
shape=Shape('compound')
turtle = Turtle(visible=False)
turtle.speed("fastest")
turtle.penup()
turtle.goto(-100,0)
turtle.begin_poly()
turtle.goto(-100,50)
turtle.goto(100,50)
turtle.goto(100,0)
turtle.goto(-100,0)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(), "yellow")
turtle.goto(-100,50)
turtle.begin_poly()
turtle.goto(0,100)
turtle.goto(100,50)
turtle.goto(-100,50)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(),"blue")
turtle.goto(-40,30)
turtle.begin_poly()
turtle.goto(-40,30)
turtle.goto(-20,30)
turtle.goto(20,0)
turtle.goto(-40,0)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(),"orange")
turtle.goto(20,20)
turtle.begin_poly()
turtle.goto(20,20)
turtle.goto(50,40)
turtle.goto(50,20)
turtle.goto(20,20)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(),"red")
screen.register_shape("house",shape)
turtle.reset()
turtle.penup()

screen.mainloop()