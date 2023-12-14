'''
Problem Statement:
Work out the first ten digits of the sum of the N 50-digit numbers.
'''

from __future__ import print_function

n = int(input().strip())

array = [int(input().strip()) for _ in range(n)]
print(str(sum(array))[:10])

