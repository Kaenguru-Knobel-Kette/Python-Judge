#!/usr/bin/env python3
import judge
from time import process_time


def line_breaks(input):
    """calculates the minimal line break penalty for a text"""
    width = input[0]
    text = input[1]
    return 42


# A&D programming exercise number
exercise = 9
# inputs from the test files
inputs = judge.read_input(exercise)
# outputs generated by the algorithm
start_time = process_time()
outputs = list()
for input in inputs:
    try:
        outputs.append([line_breaks(case) for case in input])
    except TypeError:  # in case input isn't an iterable object
        outputs.append(line_breaks(input))
end_time = process_time()

judge.verify_output(exercise, outputs, end_time - start_time)