def get_primes(seq):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True

    for num in seq:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
