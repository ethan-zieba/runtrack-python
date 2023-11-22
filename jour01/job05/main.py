#We can print here each alphabet character one by one, reversed by adding "reversed()" function
for i in (list(map(chr, reversed(range(97, 123))))):
    print(i)

#Here we can print using a step parameter of minus one, going through the list reversedly
abc = [i for i in list(map(chr, range(97, 123)))]
print(abc[::-1])

#Or just by printing it directly
print(list(map(chr, range(97, 123)))[::-1])

#Or even print them directly as a string with reversed function
#What I'm doing here is using a comprehensive list with a for loop
print(''.join(i for i in (list(map(chr, reversed(range(97, 123)))))))