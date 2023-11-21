a, b, c = input("Length of each side (a, b, c) separated by a space: ").split(" ")
a, b, c = float(a), float(b), float(c)
if a == b == c:
    print("Le triangle est équilatéral")
elif a in (b, c) or c == b:
    if a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b:
        print("Le triangle est isocèle rectangle")
    else:
        print("Le triangle est isocèle")
else:
    print("Le triangle est quelconque")