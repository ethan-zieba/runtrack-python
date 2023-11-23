L = [10,20,30,20,10,50,60,40,80,50,40]

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
#First we sort the L list
bubble(L)

listlength = 0
for e in L:
    listlength += 1
    #Using the same kind of algorithm, this time
    #comparing equality between two list elements
    for i in range(listlength):
        for j in range(0, listlength - i - 1):
            if L[j] == L[j+1]:
                del L[j]
print(L)