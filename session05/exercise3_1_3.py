import turtle
from turtle_shape import arc, circle, move, polygon


jack = turtle.Turtle()
jack.speed(0)

# large circle
circle(jack, 100)

# two arcs
move(jack, 0, 100)
jack.setheading(180)
arc(jack, 50, 180)

move(jack, 0, 100)
jack.setheading(0)
arc(jack, 50, 180)

# small circles
move(jack, 0, 50 + 100 / 6)
circle(jack, 100 / 6)

move(jack, 0, 150 + 100 / 6)
circle(jack, 100 / 6)

turtle.mainloop()
