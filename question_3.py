def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = str(item) + "_EXCEPTION"
        elif item > limit:

            modified_item = item * 2
        else:
            modified_item = item / limit
        filtered_data.append(modified_item)
        index += 1
    return filtered_data
