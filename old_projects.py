from important_functions import random_hex_color


def draw_n_eck(tur):
    n = int(input("Wie viele Ecken?\t"))
    if n > 45:
        side_length = 1
    else:
        side_length = 50
    print("Zeichne " + str(n) + "-eck...")
    angle = 360 / n

    for i in range(n):
        tur.forward(side_length)
        tur.right(angle)


def draw_spiral(tur):
    # Nimmt zwei Zahlen als Input
    n = int(input("Wie viele Spiralen?\t"))
    m = int(input("Wie lang soll die Spirale sein?\t"))

    # Zeichnet n Spiralen
    for i in range(n):
        # Zeichnet 360*(m+1) "Ecken" pro Spirale
        for ii in range(360 * (m + 1)):
            tur.forward(1)
            angle = ii / 360
            tur.right(angle)

            # Generiert eine neue #FFFFFF Farbe alle 10 Iterationen
            if ii % 10 == 0:
                r, g, b = random_hex_color()
                print("Color: " + "#" + r + g + b)
                tur.color("#" + r + g + b)

            print("Angle = " + str(angle) + "°; ii = " + str(ii) + "/" + str(360*(m+1)))
