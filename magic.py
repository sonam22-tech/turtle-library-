from turtle import *

speed(0)
bgcolor('black')
#color('aqua')
from random import choice
colors = ["red", "yellow", "green", "blue", "purple", "cyan"]
color(choice(colors))  # Choose a random color

def design():
    for i in range(500):

       # circle(150,i)
        forward(i * 2)
        #fd(i)
        right(91)
for i in range(1):
    design()
   # right(i)
hideturtle()
done()
