from settings import *


def turtle_projects():
    import turtle
    from old_projects import draw_spiral, draw_n_eck
    from important_functions import move_top_left
    from drop_simulation import random_walk

    hugo = turtle.Turtle()
    hugo.shape(shape)
    hugo.speed(speed)

    draw_n_eck(hugo)
    move_top_left(hugo)
    draw_spiral(hugo)

    random_walk(hugo)

    hugo.goto(0.00, 0.00)
    hugo.clear()


def plotting_projects():
    from schraeger_wurf import get_y, plot_template, multiple_plots
    import matplotlib.pyplot as plot

    # Typ: schraeger_wurf.plot_template
    subplots = [plot_template(velocity=1),
                plot_template(velocity=10),
                plot_template(velocity=25),
                plot_template(velocity=50)]

    multiple_plots(rows=2, columns=2, plot_list=subplots)
    plot.show()


if __name__ == "__main__":
    plotting_projects()

# input()
