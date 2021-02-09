"""
Settings
"""
import numpy as np

# Sets if debug information should be displayed
debug = True
ultra_debug = False           and debug  # requires debug to be True as well
#             ^- edit this -^

# For drop_simulation.py/random_walk:
# Selects if random moves are random of set
settings_random = False

# Settings for random = True
ran_max_moves = 1000
ran_min_moves = 100
ran_max_radius = 200
ran_min_radius = 100
ran_min_move_distance = 0

# Settings for random = False
set_moves = 200
set_radius = 200
set_min_move_distance = 0

# General settings for the turtle
speed = 3
shape = "turtle"


# Schräger Wurf
standard_v = 10
standard_start_high = 0
standard_angle_of_attack = np.deg2rad(45)
#                                     ^ Edit this
standard_gravitation_constant = 9.810
standard_list = np.arange(0, 100, 1)
standard_multiple_plots_rows = 2
standard_multiple_plots_columns = 2
