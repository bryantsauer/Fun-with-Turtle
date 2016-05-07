import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
snappy = turtle.Turtle()
snappy.speed(200)
x = 0

angle = 45

snappy.pendown() 
while x < 36: 
    angle = angle+.2
    snappy.forward(70)     
    snappy.right(angle)
    snappy.forward(10)
    snappy.right(angle)
    snappy.forward(40)
    snappy.right(angle)
    snappy.forward(80)
    snappy.right(angle)
    snappy.forward(10)
    snappy.right(angle)
    snappy.forward(100)
    snappy.right(angle)

    snappy.right(20) 
    x = x+1 # adds 1 to the value of x,
wn.exitonclick()
