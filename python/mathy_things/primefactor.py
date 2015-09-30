#!/usr/bin/env python3

from collections import Counter
from argparse import ArgumentParser

"""
A small program to calculate prime factors of a given number.
"""


def read_from_file():
    """
    returns: list of primes in primes.txt
    """
    primes = []
    try:
        f = open('primes.txt', 'r')
        for row in f:
            primes.append(int(row))
        f.close()
        return primes
    except IOError:
        print("primes.txt not found.")


def get_all_prime_factors(num_to_factor, primes):
    """
    num_to_factor: the number to factor.
    returns: Counter() of prime_factors
    """
    prime_factors = Counter()
    while num_to_factor != 0:
        prime_factors_of_left_overs, num_to_factor = \
            find_prime_factor(num_to_factor, primes)
        prime_factors.update(prime_factors_of_left_overs)
    return prime_factors


def find_prime_factor(num_to_factor, primes):
    """
    num_to_factor: num to find prime factors of.
    primes: a list of primes to use, must be primes up to num_to_factor,
        no sanity checks in place.
    returns: tuple(prime_factors,  left_over) where:
        prime_factors is primes found, and left_over is any
        non primes that were found.
    """
    prime_factors = Counter()
    for index, mod in enumerate([num_to_factor % x for x in primes]):
        if mod == 0:
            prime_factors[primes[index]] += 1
            left_over = int(num_to_factor / primes[index])
            if left_over not in primes:
                # We need to factor this number more!
                return prime_factors, left_over
            elif left_over in primes:
                prime_factors[primes[index]] += 1

    if len(prime_factors) == 0:
        return 0, 0
    return prime_factors, 0


def print_factorization(num_to_factor, factors):
    # Set our color for the result
    result = "= " + "\033[92m"
    for factor in factors:
        if factors[factor] > 1:
            result += str(factor) + "^" + str(factors[factor]) + " * "
        elif factors[factor] >= 2:
            result += str(factor) + " * "
    # Cut the the last three chars from string.
    final = result[:-3]
    # result += "\033[0m"
    print("The prime facorization is: \n", "\t |--->", num_to_factor, final)


def main():
    """
    Our main function to handle flow.
    """
    parser = ArgumentParser(
        description="Find the prime factors of a given number.")
    parser.add_argument("number",
                        help='The number to find the prime factor of.',
                        type=int)
    args = parser.parse_args()
    num_to_factor = args.number
    primes = read_from_file()
    factors = get_all_prime_factors(num_to_factor, primes)
    print_factorization(str(num_to_factor), factors)

if __name__ == '__main__':
    main()
