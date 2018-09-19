from turtle_shape import square, polygon, circle, move
import turtle

jack = turtle.Turtle()

move(jack, -100, 0)

square(jack, 100)

move(jack, 100, 0)

circle(jack, 100)

turtle.mainloop()
