#!/usr/bin/env python3
import judge
from time import process_time


def find_subarray(input):
    """finds subarrays within an array with a sliding window hash function"""
    A = input[0]
    B = input[1]
    result = ""
    m = 32768
    c = 1021
    k = len(B)
    cToK = [1]
    for i in range(0, k):
        cToK.append((cToK[i] * c) % m)
    # calculate hash B
    hash_B = 0
    for j in range(0, k):
        hash_B += B[j] * cToK[k - j - 1]
    hash_B %= m

    hash_A = 0
    for i in range(0, len(A) - len(B) + 1):
        if (i == 0):  # first hash needs to be calculated separately
            for j in range(0, k):
                hash_A += A[j] * cToK[k - j - 1]
            hash_A %= m
        else:  # calculate hash from previous one
            hash_A = (c * hash_A + A[i + k - 1] + (m - cToK[k]) * A[i - 1]) % m
        if (hash_A == hash_B):
            # verify that it isn't a false match
            is_valid = True
            for j in range(0, k):
                if A[i + j] != B[j]:
                    is_valid = False
                    break
            if is_valid:
                result += str(i) + " "
    return result + "DONE"


# A&D programming exercise number
exercise = 10
# inputs from the test files
inputs = judge.read_input(exercise)
# outputs generated by the algorithm
start_time = process_time()
outputs = list()
for input in inputs:
    try:
        outputs.append([find_subarray(case) for case in input])
    except TypeError:  # in case input isn't an iterable object
        outputs.append(find_subarray(input))
end_time = process_time()

judge.verify_output(exercise, outputs, end_time - start_time)