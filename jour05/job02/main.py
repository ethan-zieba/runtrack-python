def draw_rectangle(width, height):
    rectstring = ""
    if height != 0:
        for i in range(height):
            if i == 0:
                rectstring += f"|{'-'*int(width - 2)}|\n"
            elif i == height - 1:
                rectstring += f"|{'-'*int(width - 2)}|"
            else:
                rectstring += f"|{' '*int(width - 2)}|\n"
    else:
        rectstring = f"|{'='*int(width - 2)}|"
    print(rectstring)

draw_rectangle(10, 3)
draw_rectangle(4, 0)
draw_rectangle(0, 5)