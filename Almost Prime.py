import math
n = int(input())
count = 0
for i in range(6, n + 1):
    prime_factors = set()
    prime = 2
    num = i
    while prime <= i // 2:
        if num % prime == 0:
            prime_factors.add(prime)
            num = num // prime
        else:
            prime += 1
        
    if len(prime_factors) == 2:
        count += 1
            
print(count)