# Light-and-Schools
personal GitHub repo for the Uni Hamburg Light and Schools projet

## Projects
### Turtle
To use turtle functions, see [main.py](./main.py) function turtle_projects:
```
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
```
The turtle uses standard values defined in [the settings file](./settings.py).

### Schräger Wurf (eng.: "sloping throw")
To plot something using my framework, use the folling function in [main.py](./main.py).
```
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
```
The [plot_template()](./schraeger_wurf.py#L34) function works without arguments. It uses standard argumments which can be defined in [the settings file](./settings.py).

## Python Beginners Notebook.
