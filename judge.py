#!/usr/bin/env python3


def get_global_path():
    """returns the global path to the eclipse workspace for A&D"""
    return "/home/manuel/Documents/Algorithmen & Datenstrukturen/workspace/"


def get_exercise_name(exercise):
    """returns the folder name of the given exercise in eclipse's workspace"""
    names = {
        4: "DnA-subarraysum",
        5: "DnA-value-search",
        6: "DnA-chinese-wall-template",
    }
    return names[exercise]


def get_exercise_files(exercise):
    """returns the names of the test files for the given exercise"""
    files = {
        4: ("example1", "example2", "test1", "test2"),
        5: ("example", "test1"),
        6: ("example1", "example2", "test1", "test2"),
    }
    return files[exercise]


def read_input(exercise):
    """reads input files for the given programming exercise"""
    # path to the test files
    path = get_global_path() + get_exercise_name(exercise) + "/testdata/"
    files = get_exercise_files(exercise)

    inputs = []  # a list containing all inputs
    for file in files:
        input = []  # input from a single file
        if exercise == 4:
            with open(path + file + ".input") as fh:
                input = [int(i) for i in fh.readline().split()]
                # remove first integer because it's only for Java's Scanner
                input.remove(input[0])
        elif exercise == 5 or 6:
            with open(path + file + ".input") as fh:
                # skip first line because it's only for Java's Scanner
                fh.readline()
                input = [int(i) for i in fh.readline().split()]
        inputs.append(input)
    return inputs


def verify_output(exercise, outputs, time):
    """verifies output"""
    # path to the test files
    path = get_global_path() + get_exercise_name(exercise) + "/testdata/"
    files = get_exercise_files(exercise)

    result = []
    # save expected and actual output of each test
    for i in range(0, len(files)):
        # convert everything from the actual output to string
        output = [str(s) for s in outputs[i]]
        with open(path + files[i] + ".output") as fh:
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
        print("Your algorithm works and runs in", time, "seconds!")
        if time > 1.0:
            print("This is slow and you should find a faster solution")
