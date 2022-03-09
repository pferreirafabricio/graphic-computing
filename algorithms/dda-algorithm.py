# DDA Algorithm

def draw_line(x0, y0, x1, y1):
    dy = y1 - y0
    dx = x1 - x0
    m = dy / dx
    current_y = y0

    print(f'dy = {dy}')
    print(f'dx = {dx}')
    print(f'm = {m}')

    for index in range (x0, x1 + 1):
        print(f'x = {index}, y = {round(current_y)}')
        current_y = current_y + m

draw_line(2, 1, 7, 3)
