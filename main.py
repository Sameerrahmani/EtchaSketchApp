from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_counter_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)

def turn_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading - 5)

def clear():
    tim.reset()

screen.listen()

screen.onkeypress(move_forward, "w")
screen.onkeypress(turn_counter_clockwise, "a")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_clockwise, "d")
screen.onkeypress(clear, "c")





screen.exitonclick()
