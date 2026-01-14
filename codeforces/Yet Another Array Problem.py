import math

def get():
    line1 = input()
    a = int(line1)
    line2 = input()
    n = list(map(int, line2.split()))

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    for prime in primes:
        for num in n:
            if math.gcd(num, prime) == 1:
                return prime
            else:
                continue

    return -1

if __name__ == "__main__":
    print(get())