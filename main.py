# import colorgram
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)

# colors = colorgram.extract('image.png', 9)

rgb_colors = [(151, 89, 49), (221, 143, 78), (47, 35, 27), (21, 24, 28), (189, 134, 47), (215, 98, 55), (177, 225, 247), (240, 203, 104), (245, 217, 174)]
# first_color = colors[0]

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)

#   rgb_colors.append(new_color)

# print(rgb_colors)

def go_up():
  pass
def go_right():
  pass

def hirst():
  dot = Turtle()
  dot.up()
  #go to bottom right corner to center painting
  dot.goto(-250, -250)
  #vertical
  for _ in range(10):
    for _ in range(10):
      random_color = choice(rgb_colors)
      dot.dot(20, random_color)
      dot.forward(50)
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(180)
    dot.forward(500)
    dot.setheading(0)

hirst()

screen = Screen()
screen.exitonclick()