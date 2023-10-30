# Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
def prime_sieve_of_Eratosthenes(n1):
    prime = [True for i in range(n1+1)]
    p = 2
    while (p * p <= n1):
        if (prime[p] == True):
            for i in range(p * p, n1+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n1+1):
        if prime[p]:
            print(p)



if __name__ == "__main__":
    n1 = 10
    print(prime_sieve_of_Eratosthenes(n1))