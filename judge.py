#!/usr/bin/env python3


def run(files, outputs, time):
    """verifies that the actual output matches the expected output"""
    result = list()
    # save expected and actual output of each test
    for i in range(0, len(files)):
        # convert everything from the actual output to string
        output = [str(s) for s in outputs[i]]
        with open(files[i]) as fh:
            result.append((fh.read().splitlines(), output))
    # compare expected and actual outputs
    success = True
    for i in range(0, len(result)):
        # print tests that failed
        if result[i][0] != result[i][1]:
            print(files[i], "failed")
            print("Expected:", result[i][0])
            print("Actual:", result[i][1])
            print()
            success = False
    if success:
        print("Your algorithm passed all tests and ran in", time, "seconds!")
