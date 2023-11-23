L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

rounded = [int(e) for e in L]

print(rounded)

listlength = 0
    #Calculating length of list, since we can't use "len()"
for e in rounded:
    listlength += 1
#For each index of the list...
for i in range(listlength):
#...we go through each index of the list between 0 and the indexes
#already sorted, meaning the largest number is already at the end position
    for j in range(0, listlength - i - 1):
        if rounded[j] > rounded[j+1]:
            rounded[j], rounded[j+1] = rounded[j+1], rounded[j]

print(rounded)