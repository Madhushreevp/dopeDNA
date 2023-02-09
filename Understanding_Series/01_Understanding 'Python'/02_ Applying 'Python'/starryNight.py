# starry night

import turtle as t
# module used for drawing different shapes and pictures
from random import randint, random
# module used for generating random paramenters

size = 300
points = 5
angle = 144
# define legth,angle and size to lay a star

def draw_star(points, size, col, x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.color('yellow')
	t.begin_fill()
	# define colour of the star,by filling colour in it

	for i in range(points):
		 t.forward(size)
		 t.right(angle)
	# drawing a star with given specs

	t.end_fill()


# Main code
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow', 0, 0)
t.hideturtle()
while True:
	 ranPts = randint(2, 5) * 2 + 1
	 ranSize = randint(10, 50)
	 ranCol = (random(), random(), random())
	 ranX = randint(-350, 300)
	 ranY = randint(-250, 250)
	 draw_star(ranPts, ranSize, ranCol, ranX, ranY)
	 
 
 
