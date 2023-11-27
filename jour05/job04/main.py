def tapis(height):
    tapstring = f"+{'-'*(height+1)}+\n"
    for i in range(height+2):
        if i is not height+1:
            tapstring += f"|{'#'*(height-i)+' '+'#'*(i)}|\n"
        else:
            tapstring += f"+{'-'*(height+1)}+"
    print(tapstring)

tapis(10)