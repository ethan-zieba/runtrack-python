def even_odd(nombre):
    if type(nombre) is not int:
        return "ERROR: not an integer"
    if nombre % 2 == 0:
        return "Le nombre est pair"
    else:
        return "Le nombre est impair"

print(even_odd(10))
print(even_odd(9))
print(even_odd(12.5))
print(even_odd(5))
