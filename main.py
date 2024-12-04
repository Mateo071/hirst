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

def reset_position(dot, x):
    horizontal_gap = int(x * 50)
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(180)
    dot.forward(horizontal_gap)
    dot.setheading(0)

def go_right(dot, x):
  for _ in range(x):
      random_color = choice(rgb_colors)
      dot.dot(20, random_color)
      dot.forward(50)

def hirst(x, y):
  dot = Turtle()
  dot.hideturtle()
  dot.up()
  dot.speed(0)
  #go to bottom right corner to center painting

  horizontal_starting_point = int((-x * 50) / 2)
  vertical_starting_point = int((-y * 50) / 2)
  dot.goto(horizontal_starting_point, vertical_starting_point)
  #vertical
  for _ in range(y):
    go_right(dot, x)
    reset_position(dot, x)

def prompt():
  print("Welcome to the spot art maker - Inspired by Damien Hirst.")
  rows = int(input("How many rows would you like to have?: "))
  columns = int(input("How many columns would you like to have?: "))

  hirst(rows, columns)

prompt()

screen = Screen()
screen.exitonclick()