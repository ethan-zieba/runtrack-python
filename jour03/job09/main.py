def moyenne(a, b ,c):
    return (a + b + c)/3

moyenne_etudiant = moyenne(15, 18, 20)

if 20 >= moyenne_etudiant >= 15:
    print("Très bon élève")
elif 15 > moyenne_etudiant >= 11:
    print("Bon élève")
elif 11 > moyenne_etudiant >= 8:
    print("Élève moyen")
elif 8 > moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")
