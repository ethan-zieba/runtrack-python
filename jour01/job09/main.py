#For an inventory ressources management program,
#we'll use objects as python is an OOP (object oriented programming) language

class Product():
    #Here we initialize the class attributes
    def __init__(self, n, p, q):
        self.name = str(n)
        self.price = float(p)
        self.quantity = int(q)

    #We use a method to return the attributes so we don't have to modify them by calling
    #them directly
    def get_infos(self, attribut=None):
        if attribut is None:
            return("Nom: " + self.name + "\nPrix: " + str(round(self.get_infos("price")), 2) + "€" + "\nQuantité: " + str(self.quantity))
        return getattr(self, attribut)

    #We use a method to set the attributes
    def set_infos(self, newn=None, newp=None, newq=None):
        if newn is not None:
            self.name = newn
        if newp is not None:
            self.price = round(newp, 2)
        if newq is not None:
            self.quantity = newq

    def buy(self, bqty):
        #We check here if there's enough stock
        if self.get_infos("quantity") - bqty >= 0:
            if input("Total cost: " + str(bqty * self.price) + " Confirm buy ? y/n").lower() == "y":
                self.set_infos(newq= self.get_infos("quantity") - bqty)
                return("New " + self.get_infos("name") + " quantity: " + str(self.get_infos("quantity")))
        else:
            return("[ERROR]: Not enough stock")

inventaire = [Product("Eau", 0.1, 12), Product("Sel", 20, 53), Product("Combat Patrol Warhammer", 125, 4),
              Product("Le Canada", 2, 1)]

exit = False;
while exit != True:
    print("Products list:\n" + str([(i.get_infos("name"), "Prix: " + str(i.get_infos("price")) + "€") for i in inventaire]))
    print(inventaire[int(input("Product to buy: "))].buy(int(input("Quantity: "))))
    if input("Exit ? y/n").lower() == "y":
        exit = True

#Increase prices by 10%
for i in inventaire:
    i.set_infos(newp=(i.get_infos("price")*1.1))
print("Products list:\n" + str([(i.get_infos("name"), "Prix: " + str(i.get_infos("price")) + "€") for i in inventaire]))
