from question_4_a import *


def mut1(data, limit, exceptions):
    filtered_data = []
    index = 0
    # Changed the multiplciation and division
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = str(item) + "_EXCEPTION"
        elif item > limit:
            modified_item = item / limit
        else:
            modified_item = item * 2
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


def mut2(data, limit, exceptions):
    filtered_data = []
    index = 0
    # Removed the exceptions
    while index < len(data):
        item = data[index]
        if item > limit:

            modified_item = item * 2
        else:
            modified_item = item / limit
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


def mut3(data, limit, exceptions):
    filtered_data = []
    index = 0
    # Removed the multiplication part
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = str(item) + "_EXCEPTION"
        else:
            modified_item = item / limit
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


def mut4(data, limit, exceptions):
    filtered_data = []
    index = 0
    # multiply each time
    while index < len(data):
        item = data[index]
        modified_item = item * 2
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


def mut5(data, limit, exceptions):
    filtered_data = []
    index = 0
    # divide every time
    while index < len(data):
        item = data[index]
        modified_item = item / limit
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


def mut6(data, limit, exceptions):
    return [i * 2 if i > limit else i / limit for i in data]
