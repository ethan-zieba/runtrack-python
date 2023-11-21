n = input("Entrez un entier supérieur à 0: ")

for i in range(1, int(n) + 1):
    print("Table de multiplication de {}".format(i))
    for u in range(1, 11):
        print("{} x {} = {}".format(i, u, (i*u)))
    print("\n")