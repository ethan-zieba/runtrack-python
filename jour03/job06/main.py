def is_positive(num):
    if num == 0:
        return "Le nombre est nul"
    elif num > 0:
        return "Le nombre est positif"
    elif num < 0:
        return "Le nombre est négatif"

print(is_positive(120))
print(is_positive(-120))
print(is_positive(0))