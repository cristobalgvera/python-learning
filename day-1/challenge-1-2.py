def calculatePrime():
    primes_sum = 0

    for i in range(1, 101, 1):
        for j in range(1, i + 1, 1):
            if i % j == 0 and j != 1 and j != i:
                break
            elif i == j and i != 1:
                print('Prime:', i)
                primes_sum += i

    print(primes_sum)


calculatePrime()
