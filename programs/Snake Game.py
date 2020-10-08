# This is a simple snake game
# Using the basic

import turtle
import time
import random

delay = 0.2

# score
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
wn.title("Snake Game @ Ascad Bin Abubakar")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 275)
pen.write("Score : 0 \t\t\t\t  High Score: 0", align='center', font=("Courior", 16, "normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# main game loop
while True:
    wn.update()
    
    # Check for a collison with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hide the segment
        for segment in segments:
            segment.goto(1000, 1000)
        
        # clear the segment
        segments.clear()
        
        # Reset the score
        score = 0
        
        # Reset the delay
        delay = 0.2
        
        # Reset the food into its original position
        food.goto(0, 100)
        
        # Update the screen display
        pen.clear()
        pen.write("Score : {} \t\t\t  High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))
    
    # Check for a collison with the food
    if head.distance(food) < 20:
        
        # move the food to a randam position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shortand the delay
        delay -= 0.001
        
        # increase the score
        score += 10
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score : {} \t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))
    
    # Move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # check for the head collision with the segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide the segment
            for segment in segments:
                segment.goto(1000, 1000)
            
            # clear the segment
            segments.clear()
            
            # Reset the score
            score = 0
            
            # Reset the delay
            delay = 0.2
            
            # Reset the food into its original position
            food.goto(0, 100)
            
            # Update the screen display
            pen.clear()
            pen.write("Score : {} \t\t\t  High Score: {}".format(score, high_score), align='center',
                      font=("Courior", 16, "normal"))
            
            # Reset the food into its original position
            food.goto(0, 100)
    
    time.sleep(delay)
wn.mainloop()
