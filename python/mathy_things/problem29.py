#!/usr/bin/env python3
from itertools import product
"""
Problem 29: https://projecteuler.net/problem=29
Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125
    If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

bunch_of_nums = []
# Apparently Pep8 says this is antipattern, doing it just for fun.
squared = lambda a, b: a**b
for num in product(range(100, 1, -1), range(100, 1, -1)):
    bam = squared(*num)
    if bam not in bunch_of_nums:
        bunch_of_nums.append(bam)
print(len(bunch_of_nums))
