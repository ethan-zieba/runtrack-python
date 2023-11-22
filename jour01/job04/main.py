#We can print here each alphabet character one by one
#The map function is used here to apply the "chr" function (that returns a character when its
#unicode index is provided) to each number of the 97-123 range (corrsponding to the lowercase alphabet in unicode)
for i in (list(map(chr, range(97, 123)))):
    print(i)

#Or print them directly as a list
print(list(map(chr, range(97, 123))))

#Or even print them directly as a string
#What I'm doing here is using a comprehensive list with a for loop
print(''.join(i for i in (list(map(chr, range(97, 123))))))