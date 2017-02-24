#!/usr/bin/env python3
import os
import judge
from time import process_time


def read_input():
    inputs = list()  # a list containing inputs from all files
    for file in input_files:
        with open(file) as fh:
            fh.readline()  # skip line because it's only for Java's Scanner
            input = [int(i) for i in fh.readline().split()]
        inputs.append(input)
    return inputs


def f(x):
    """special function that should be treated as blackbox"""
    r = 0
    z = x
    while z > 0:
        r += x
        z = int(z / 2)
    return r


def value_search(a):
    """binary function value search"""
    result = []
    for i in range(0, len(a)):
        l = 0
        r = 20000000
        while l <= r:
            x = (l + r) // 2
            if f(x) == a[i]:
                break
            if f(x) < a[i]:
                l = x + 1
            else:
                r = x - 1
        else:
            result.append("NO")
            continue
        result.append(x)
    return result


# path to the local test files
path = "testdata/DnA-binary-value-search/"
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
    outputs.append(value_search(input))
end_time = process_time()

judge.run(output_files, outputs, end_time - start_time)
