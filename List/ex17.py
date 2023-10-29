# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

def check_prime(n):
    if n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
            break
        return True


if __name__ == "__main__":
    print(all(list(map(check_prime, [0, 3, 4, 7, 9]))))
    print(all(list(map(check_prime, [3, 5, 7, 13]))))
    print(all(list(map(check_prime, [1, 5, 3]))))
