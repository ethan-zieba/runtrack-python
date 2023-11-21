for i in range(1, 1001):
    not_prime = False
    for u in range(2, i):
        if i % u == 0:
            not_prime = True
            break
    if not_prime == False and i != 1:
        print(i)