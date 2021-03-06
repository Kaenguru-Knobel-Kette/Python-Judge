#!/usr/bin/env python3
import os
import judge
from time import process_time


def read_input():
    inputs = list()  # a list containing inputs from all files
    for file in input_files:
        input = list()  # input from a single file
        with open(file) as fh:
            fh.readline()  # skip line because it's only for Java's Scanner
            input.append([int(i) for i in fh.readline().split()])
            fh.readline()  # skip line because it's only for Java's Scanner
            input.append([int(i) for i in fh.readline().split()])
        inputs.append(input)
    return inputs


def match_ribbons(input):
    lengths = input[0]
    areas = input[1]
    i = 0  # index iterating over areas
    count = 0
    for l in lengths:
        l = l ** 2 / 16
        # a ribbon fits if sqrt(a) == l/4 or a == l^2/16
        while areas[i] < l and i < len(areas) - 1:
            i += 1
        if areas[i] == l:
            # ribbon fits, advance to next ribbon
            i += 1
            count += 1
    return [count]


# path to the local test files
path = "testdata/DnA-presents/"
input_files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".input")]
output_files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".output")]
input_files.sort()
output_files.sort()
# inputs from the test files
inputs = read_input()
# outputs generated by the algorithm
start_time = process_time()
outputs = list()
for input in inputs:
    outputs.append(match_ribbons(input))
end_time = process_time()

judge.run(output_files, outputs, end_time - start_time)
