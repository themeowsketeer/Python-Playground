# Execution time: O(n log log n)
# Sieve of Eratosthenes algorithms, used to generate a set of prime up to n-1. 
# In the array, any index with value 0 is a prime.
def sieve_1(n):
    sieve = [0] * n
    for i in range(2,n):
        if (sieve[i] != 0):
            continue
        for u in range(2*i, n, i):
            sieve[u] = 1
    for i in range(1,n):
        print(f'{i}: {sieve[i]}')

# Extended Sieve of Eratosthenes algorithms, used to generate a set of prime up to n-1.
# In the array, every numeric index has value being its smallest prime factor, excluding common factor 1
def sieve_2(n):
    sieve = [1] * n # Every number starts with a common factor of 1
    for i in range(2,n):
        if (sieve[i] != 1):
            continue
        else: sieve[i] = i
        for u in range(2*i, n, i):
            sieve[u] = i
    for i in range(1,n):
        print(f'{i}: {sieve[i]}')

print(sieve_1(40))