#!/usr/bin/env python3

from sys import argv
# take input


def find_prime(maxvalue):
    primes = [2, 3, 5]
    for num in range(7, int(maxvalue), 6):
        if is_prime(num, primes):
            primes.append(num)
        if is_prime(num + 4, primes) and (num + 4) < maxvalue:
            primes.append(num + 4)
    return primes


# is prime
def is_prime(num, primes):
    """
    num: number to check if it's prime.
    primes: 
    """
    if 0 not in [num % x for x in primes]:
        return True
    else:
        return False


def write_to_file(rows):
    """
    Takes a list, and writes to disk, as a row for each item in list.
    """
    f = open('primes.txt', 'w')
    for row in rows:
        f.write(str(row) + '\n')
    f.close


def main():
    if len(argv) != 2:
        print(
            "Invalid number or arguments.",
            "{} requires 1 argument, ".format(argv[0]) +
            "the max number upto to find primes of.", sep="\n")
        exit()
    elif len(argv) == 2:
        primes = find_prime(int(argv[1]))
        write_to_file(primes)
    else:
        print("Unknown error has occured.")

if __name__ == '__main__':
    main()
