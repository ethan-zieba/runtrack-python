def triangle(height):
    tristring = ""
    for i in range(height):
        if i is not height-1:
            tristring += f"{' '*int(height-i)}/{' '*(i*2)}\\\n"
        else:
            tristring += f"{' '*int(height-i)}/{'_'*(i*2)}\\\n"
    print(tristring)

triangle(10)