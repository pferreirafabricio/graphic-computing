# Bresenham algorithm

def draw_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * (dy - dx)
    increE = 2 * dy
    increNE = 2 * dy - dx
    x = x0
    y = y0

    print(f'x = {x}, y = {y}')

    while(x < x1):
        if (d < 0):
            d += increE
            x += 1
        else:
            d += increNE
            x += 1
            y += 1
        
        print(f'x = {x}, y = {y}')

draw_line(2, 1, 7, 3)
