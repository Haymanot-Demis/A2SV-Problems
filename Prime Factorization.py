testcases = int(input())
sum_of_prime_factors = 0
for _ in range(testcases):
    n = int(input())
    d = 2
    prime_factors = []
    while n > 1:
        isPrime = True
        while d <= n ** 0.5:
            if n % d == 0:
                prime_factors.append(d)
                n //= d
            else:
                d += 1
        if isPrime:
            prime_factors.append(n)
            n //= n
    print(prime_factors)
    sum_of_prime_factors += sum(prime_factors)   
print(sum_of_prime_factors)