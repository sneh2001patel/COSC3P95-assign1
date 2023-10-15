from question_5 import *


def delta_debugging(test_case, chunk_size):
    if chunk_size <= 1:
        return test_case

    i = 0
    while i < len(test_case):
        new_test_case = (test_case[0][:i] + test_case[0][i + chunk_size:],
                         test_case[1][:i] + test_case[1][i + chunk_size:])

        # print(new_test_case, chunk_size, start)
        if is_bug(new_test_case):
            test_case = new_test_case
        else:
            i += chunk_size

    # Reduce the chunk size
    chunk_size = chunk_size // 2
    return delta_debugging(test_case, chunk_size)


def is_bug(test_case):
    # Return true if bug else return false
    output = processString(test_case[0])
    if output != test_case[1]:
        return True
    else:
        return False
    # return 'bug' in test_case


test_cases = {
    ("abcdefG1", "ABCDEFg1"),
    ("CCDDEExy", "ccddeeXY"),
    ("1234567b", "1234567B"),
    ("8665", "8665"),
}
for test_case in test_cases:
    reduced_test_case = delta_debugging(test_case, len(test_case[0]) // 2)
    print("Initial Test Case:", test_case)
    print("Reduced Test Case:", reduced_test_case)