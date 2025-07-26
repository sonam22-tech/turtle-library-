from colorsys import hsv_to_rgb
from turtle import *
speed(0)
bgcolor('black')
h=0
#color=["red","yellow","green","blue","aqua","pink"]
for i in range(200):
    color(hsv_to_rgb(h,1,1))
    h+=0.014
    rt(i)
    circle(150,i)
    fd(i)
    rt(90)
hideturtle()
done()