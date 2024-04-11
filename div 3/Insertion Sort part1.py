#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    key_int = arr[-1]
    i = n - 2  # Start from the second-to-last element
    while (i >= 0 and arr[i] > key_int):
        arr[i + 1] = arr[i]  # Shift elements to the right
        i -= 1
        print(" ".join(map(str, arr)))  # Print the array at each step
    arr[i + 1] = key_int  # Insert the key at the correct position
    print(" ".join(map(str, arr)))  # Print the final sorted array

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
