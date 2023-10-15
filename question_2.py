import random

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'


# For this question I am using the merge sort
# Function divides the array into 2 parts thru the middle
def divide(arr):
    if len(arr) > 1:
        temp = (len(arr) // 2)  # get middle point // ensures we get a int
        left = arr[:
                   temp]  # left array contains all elements from 0 to middle point
        right = arr[
            temp:]  # right array contains all elements from middle point + 1 till end

        # repeat until each element has an array of its own
        left = divide(left)
        right = divide(right)
        return merge(left, right)
    else:
        return arr


def merge(left, right):
    output = []
    i, j = 0, 0

    # loop thru the two left, and right array
    while i < len(left) and j < len(right):
        # if left side is smaller than the right side put add that
        if left[i] > right[j]:
            # the less than produces an array in accessending order for decending order change '<' to '>'
            output.append(left[i])
            i += 1
        else:
            # if right side is smaller than the left side add that
            output.append(right[j])
            j += 1

    # Add the remain pieces from left and right
    while i < len(left):
        output.append(left[i])
        i += 1
    while j < len(right):
        output.append(right[j])
        j += 1
    return output


def ground_truth(arr):
    return sorted(arr)


def random_test_gen():
    EPOCHS = 5
    for _ in range(EPOCHS):
        arr_length = random.randint(0, 10)
        input_arr = []
        for _ in range(arr_length):
            input_arr.append(random.randint(1, 20))
        input_data = input_arr
        expected_output = ground_truth(input_arr)
        # run the function we were testing
        output = divide(input_data)
        # check if the output matches the expected output
        if output != expected_output:
            print(
                f"{FAIL}Test case Fail{ENDC} \n Input:{input_data}, \n Expected: {expected_output} \n Actual: {output}"
            )
        else:
            print(
                f"{OKGREEN}Test case Pass{ENDC} \n Input:{input_data} \n Expected: {expected_output} \n Actual: {output}"
            )


def all_test_gen(test_cases):
    for test in test_cases:
        input_data = test[0]
        expected_output = test[1]
        # run the function we were testing
        output = divide(input_data)
        # check if the output matches the expected output
        if output != expected_output:
            print(
                f"{FAIL}Test case Fail{ENDC} \n Input:{input_data}, \n Expected: {expected_output} \n Actual: {output}"
            )
        else:
            print(
                f"{OKGREEN}Test case Pass{ENDC} \n Input:{input_data} \n Expected: {expected_output} \n Actual: {output}"
            )


random_test_gen()
# all_test_gen(test_cases=test_cases)
