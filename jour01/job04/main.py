#We can print here each alphabet character one by one
for i in (list(map(chr, range(97, 123)))):
    print(i)

#Or print them directly as a list
print(list(map(chr, range(97, 123))))

#Or even print them directly as a string
#What I'm doing here is using a comprehensive list with a for loop
print(''.join(i for i in (list(map(chr, range(97, 123))))))