abc = ''.join(list(map(chr, range(97, 123)))*10)

for i in range(len(abc)):
    print(abc[0:i])