import turtle

n = int(input('enter the sides of a polygon'))
side = int(input('enter the length of a polygon'))
def draw_polygon():
    for variable in range(0, n):
        turtle.forward(side)
        turtle.right(360 / n)

draw_polygon()
turtle.penup()
turtle.goto(80, 100)
turtle.pendown()
draw_polygon()