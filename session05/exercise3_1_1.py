from turtle_shape import arc, circle, move, polygon
import turtle
import math

# 3.1.1

jack = turtle.Turtle()
jack.speed(0)

# large circle
circle(jack, 100)

# 4 triangles
move(jack, 0, 100)
jack.setheading(60)
polygon(jack, 3, 100)
jack.setheading(150)
polygon(jack, 3, 100)
jack.setheading(240)
polygon(jack, 3, 100)
jack.setheading(330)
polygon(jack, 3, 100)


# 4 small circles
moving_step = 50 * math.sqrt(3)
small_radius = 50 * math.sqrt(3) / 3

move(jack, 0, 100 - moving_step)
jack.setheading(0)
circle(jack, small_radius)

move(jack, moving_step, 100)
jack.setheading(90)
circle(jack, small_radius)

move(jack, 0, 100 + moving_step)
jack.setheading(180)
circle(jack, small_radius)

move(jack, -moving_step, 100)
jack.setheading(270)
circle(jack, small_radius)


turtle.mainloop()
