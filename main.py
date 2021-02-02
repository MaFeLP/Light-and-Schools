import turtle

from old_projects import *
# draw_n_eck(hugo)
# move_top_left(hugo)
# draw_spiral(hugo)

from drop_simulation import random_walk

from settings import *

hugo = turtle.Turtle()
hugo.shape(shape)
hugo.speed(speed)


# hugo.goto(0.00, 0.00)
# hugo.clear()

if __name__ == "__main__":
    random_walk(hugo)
