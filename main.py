start_list = [-1, -8, 3, 5, 4, 4, 9, 8, 3, 6, 5, 7, 2, 0, -3, 10]


def algorithm(data):
    out_list = []  # Init output list

    for i in range(min(data), max(data) + 1):  # Main Cycle
        out_list += [i] * data.count(i)  # Mechanism of "sort"

    return out_list  # Return output


result = algorithm(start_list)
print(result)
