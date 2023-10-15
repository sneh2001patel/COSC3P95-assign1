def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2  # bug here: since number is a string * 2 creates a copy of that number therfore if the string was x1 it becomes X11
        else:
            output_str += char.upper()
    return output_str
