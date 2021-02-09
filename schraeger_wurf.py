import numpy as np
import matplotlib.pyplot as plot

from settings import standard_gravitation_constant, standard_v, standard_angle_of_attack, standard_start_high,\
    standard_list, standard_multiple_plots_rows, standard_multiple_plots_columns, \
    debug, ultra_debug


# Calculates y of "ball" of an x.
def get_y(x,  # x to get the y of
          start_high=standard_start_high,  # height at which the ball was thrown
          velocity=standard_v,  # velocity with which the ball flies
          angle_of_attack=standard_angle_of_attack,  # angle at which the ball was thrown
          gravitation_constant=standard_gravitation_constant):  # gravitation constant in europe is 9.810

    out = round((start_high + (np.tan(angle_of_attack) * x) -
                 (gravitation_constant / (2 * velocity ** 2 * (np.cos(angle_of_attack)) ** 2)) * x ** 2),
                2)

    if ultra_debug:
        print(f"------------Ultra-Debug Info--------------\n"
              f"> Function: \t\t\"schraeger_wurf.get_y\"\n"
              f"> x:\t\t\t\t{x}\n"
              f"> start height:\t{start_high}\n"
              f"> Velocity\t\t\t{velocity}\n"
              f"> Angle of Attack\t{angle_of_attack}\n"
              f"> Gravitation\t\t{gravitation_constant}\n"
              f"> Result:\t\t\t{out}\n"
              f"-------------------------------------------")
    return out


# Create a template which you can plot, if you have split up the results before
def plot_template(x_list=standard_list,  # list with all x values to plot
                  start_high=standard_start_high,  # height at which the ball was thrown
                  velocity=standard_v,  # velocity with which the ball flies
                  angle_of_attack=standard_angle_of_attack,  # angle at which the ball was thrown
                  gravitation_constant=standard_gravitation_constant,  # gravitation constant in europe is 9.810
                  symbol="-"):  # Symbol which will be used to plot points. "-" draws a line
    # Creates a list with all y-values for each x-value
    y_values = []
    for i in x_list:
        y_i = get_y(x=i, start_high=start_high, velocity=velocity,
                    angle_of_attack=angle_of_attack, gravitation_constant=gravitation_constant)
        # Only add the value if ball is not under the ground, else add 0 as height
        if y_i > 0:
            y_values.append(y_i)
        else:
            y_values.append(0)

        if ultra_debug:
            print(f"------------Ultra-Debug Info-------------------\n"
                  f"> Function: \t\t\"schraeger_wurf.plot_template\"\n"
                  f"> i in x_list:\t\t{i}\n"
                  f"> y(i):\t\t\t{y_i}\n"
                  f"> Velocity\t\t\t{velocity}\n"
                  f"> Angle of Attack\t{angle_of_attack}\n"
                  f"> Gravitation\t\t{gravitation_constant}\n"
                  f"> x_list:\t\t{x_list}\n"
                  f"> y_values:\t\t{y_values}"
                  f"------------------------------------------------")

    if debug:
        print(f"------------------Debug Info-------------------\n"
              f"> Function: \t\t\"schraeger_wurf.plot_template\"\n"
              f"> start_high:\t\t\t{start_high}\n"
              f"> Velocity\t\t\t{velocity}\n"
              f"> Angle of Attack\t{angle_of_attack}\n"
              f"> Gravitation\t\t{gravitation_constant}\n"
              f"> Symbol:\t\t\t{symbol}\n"
              f"------------------------------------------------")

    return x_list, y_values, symbol


# Create multiple subplots in one general plot.
# Preparation for this:
def multiple_plots(rows=standard_multiple_plots_rows,
                   columns=standard_multiple_plots_columns,
                   plot_list=plot_template()):
    # Prevents from having more than the desired empty plots
    if len(plot_list) == 1:
        rows = 1
        columns = 1

    fig, ax = plot.subplots(nrows=rows, ncols=columns)

    i = 0
    # creates subplots and lists them in the plot
    for row in ax:
        for col in row:
            # Prevents from throwing an error, when the end of the plots is reached
            if i > len(plot_list):
                break
            x, y, symbol = plot_list[i]
            col.plot(x, y, symbol)
            i += 1

        # Prevents from throwing an error, when the end of the plots is reached
        if i > len(plot_list):
            break

    if debug:
        print(f"------------------Debug Info-------------------\n"
              f"> Function: \t\"schraeger_wurf.multiple_plots\"\n"
              f"> rows:\t\t\t{rows}\n"
              f"> y_values:\t\t{columns}\n"
              f"------------------------------------------------")
