def randomsize(m):
    prime_number = []
    count = 2
    
    while count < 30:
        isprime = True
        
        for x in range(2, int(count ** (1/2) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            prime_number.append(count)
        
        
        count += 1

    sliced_prime_number = []
    random_number = [5, 8, 1, 9, 6, 10, 7, 3, 2, 4]
    sliced_index = random_number[:m]
    total = 0
    for i in sliced_index:
        sliced_prime_number.append(prime_number[i])
        total += prime_number[i]
    return print(sliced_prime_number, '\n', 'sum: ', total)