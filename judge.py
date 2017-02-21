#!/usr/bin/env python3


def get_exercise_path(exercise):
    """returns the path to the test files of the given exercise"""
    names = {
        4: "DnA-maximum-subarray-sum",
        5: "DnA-binary-value-search",
        6: "DnA-chinese-wall-parking",
        7: "DnA-presents",
        8: "DnA-wind-turbines",
        9: "DnA-line-breaks",
        10: "DnA-find-subarray",
    }
    return "testdata/" + names[exercise] + "/"


def get_exercise_files(exercise):
    """returns the names of the test files for the given exercise"""
    files = {
        4: ("example1", "example2", "test1", "test2"),
        5: ("example", "test1"),
        6: ("example1", "example2", "test1", "test2"),
        7: ("example1", "test1", "test2", "test3"),
        8: ("example", "test1", "test2"),
        9: ("example", "test1", "test2", "test3"),
        10: ("example", "test1", "test2", "test3"),

    }
    return files[exercise]


def read_input(exercise):
    """reads input files for the given programming exercise"""
    files = get_exercise_files(exercise)  # path to the test files

    inputs = list()  # a list containing inputs from all files
    for file in files:
        input = list()  # input from a single file
        with open(get_exercise_path(exercise) + file + ".input") as fh:
            if exercise == 4:
                input = [int(i) for i in fh.readline().split()]
                # remove first integer because it's only for Java's Scanner
                input.remove(input[0])
            elif exercise == 5 or exercise == 6:
                fh.readline()  # skip line because it's only for Java's Scanner
                input = [int(i) for i in fh.readline().split()]
            elif exercise == 7:
                fh.readline()  # skip line because it's only for Java's Scanner
                input.append([int(i) for i in fh.readline().split()])
                fh.readline()  # skip line because it's only for Java's Scanner
                input.append([int(i) for i in fh.readline().split()])
            elif exercise == 8:
                for i in range(0, int(fh.readline())):
                    D = int(fh.readline().split()[1])
                    d = tuple([int(i) for i in fh.readline().split()])
                    e = tuple([int(i) for i in fh.readline().split()])
                    input.append((D, d, e))
            elif exercise == 9:
                for i in range(0, int(fh.readline())):
                    first_line = [int(i) for i in fh.readline().split()]
                    width = first_line[1]
                    text = tuple([fh.readline()[0:-1] for i in range(0, first_line[0])])
                    input.append((width, text))
            elif exercise == 10:
                for i in range(0, int(fh.readline())):
                    fh.readline()  # skip line because it's only for Java's Scanner
                    A = tuple([int(i) for i in fh.readline().split()])
                    B = tuple([int(i) for i in fh.readline().split()])
                    input.append((A, B))
            # add input from the file as tuple
            inputs.append(tuple(input))
    return inputs


def verify_output(exercise, outputs, time):
    """verifies output"""
    files = get_exercise_files(exercise)  # path to the test files

    result = list()
    # save expected and actual output of each test
    for i in range(0, len(files)):
        # convert everything from the actual output to string
        output = [str(s) for s in outputs[i]]
        with open(get_exercise_path(exercise) + files[i] + ".output") as fh:
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
        if time > 0.1:
            print("This is slow and you should find a faster solution")
