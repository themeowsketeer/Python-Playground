def sym(*arg):
    unique = []
    for i in range(0,len(arg)):
        unique += arg[i]
    unique = set(unique)
    result = []
    for check in unique:
        count = 0
        for i in range(0,len(arg)):
            if (check in arg[i]):
                count+=1
        if (count == 1):
            result.append(check)
        else: continue
    print(result)
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])