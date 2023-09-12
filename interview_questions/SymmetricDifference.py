def sym_2_arrays(arg1, arg2):
    unique = set(arg1 + arg2)
    result = []
    for check in unique:
        if ((check in arg1) and (check in arg2)):
            continue
        else: result.append(check)
    return result

def sym(*arg):
    result = sym_2_arrays(arg[0], arg[1])
    for i in range(2, len(arg)):
        result = sym_2_arrays(result, arg[i])
    print(result)

sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])