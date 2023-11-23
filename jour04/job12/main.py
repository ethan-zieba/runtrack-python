import random
#Generating list of 30 random numbers
L = [random.randint(1, 100) for i in range(30)]
print(L)

#Here using a bubble sort algorithm
def bubble(liste):
    listlength = 0
    #Calculating length of list, since we can't use "len()"
    for e in liste:
        listlength += 1
    #For each index of the list...
    for i in range(listlength):
        #...we go through each index of the list between 0 and the indexes
        #already sorted, meaning the largest number is already at the end position
        for j in range(0, listlength - i - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
bubble(L)
print(L)