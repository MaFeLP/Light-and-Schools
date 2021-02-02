import math
import random

from important_functions import random_hex_color

from settings import *


def pythagoras(a, b):
    return math.sqrt((a * a) + (b * b))


def pythagoras_tuple(ab):
    a, b = ab
    return math.sqrt((a * a) + (b * b))


# Nimmt eine Schilkröte und einen Radius.
# Die Schildkröte zeichnet einen Kreis (mit Radius) um (0|0) und bewegt sich beliebig oft dort drin.
def random_walk(tur):
    if settings_random:
        # Generiert zufälligen Radius und Anzahl an Bewegungen
        walks = random.randint(0, ran_max_moves)
        radius = random.randint(0, ran_max_radius)
        # Generiert einn maximalen bewegungsradius
        max_move_distance = random.randint(ran_min_move_distance, radius)
        print("Hugo darf sich maximal " + str(max_move_distance) + " bewegen!")

    else:
        walks = set_moves
        radius = set_radius
        max_move_distance = random.randint(set_min_move_distance, radius)
        print("Hugo darf sich maximal " + str(max_move_distance) + " bewegen!")

    # zeichnet einen Kreis in hellgrün um (0|0)
    print("Zeichne Kreis mit Radius " + str(radius) + " um (0|0)...")
    tur.penup()
    x, y = tur.pos()
    tur.goto(0.00, 0.00)
    tur.goto(x, y - radius)
    tur.pendown()
    tur.color("#00FF00")
    tur.circle(radius=radius)
    tur.penup()
    tur.goto(0.00, 0.00)
    tur.pendown()

    escapes = 0

    # Schleife läuft so lange wie es walks gibt.
    for i in range(walks):
        # weist der der Schildkröte eine zufällige Farbe zu.
        r, g, b = random_hex_color()
        tur.color("#" + r + g + b)

        # Speichert die Position der Schildkröte für x in pos_x und für y in pos_y
        pos_x, pos_y = tur.pos()
        # Generiert einen zufälligen Abstand zu der neuen Position (Delta x, Delta y)
        d_x = random.randint(-max_move_distance, max_move_distance)
        d_y = random.randint(-max_move_distance, max_move_distance)

        # Wenn die neue Position ausßerhalb des Radiuses liegt:
        if pythagoras(pos_x + d_x, pos_y + d_y) >= radius:
            print("Hugo versuchte zu entkommen! Erwischt!")
            escapes += 1
            print("Hugo versuchte schon " + str(escapes) + "mal zu entkommen!\n")
            continue  # Fahre mit der nächsten Schleifeniteration fort.

        # Bewege die Schildkröte zur neuen Position
        tur.goto(pos_x + d_x, pos_y + d_y)

        # gebe Debuginfos aus.
        if debug:
            print("Farbe:\t\t\t\t" + "#" + r + g + b)
            print("Radius von (0|0):" + "\t" + str(pythagoras_tuple(tur.pos())))
            print("Position:\t\t\t(" + str(pos_x + d_x) + "|" + str(pos_y + d_y) + ")")
            print("Bewegungen:\t\t\t" + str(i) + "/" + str(walks))
            print()

    print("Hugo versuchte " + str(escapes) + "mal zu entkommen!")
