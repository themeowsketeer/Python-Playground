def pairwise(arr, arg):
    result = 0
    usedIndex = set()
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (((arr[i] + arr[j]) == arg) and i not in usedIndex and j not in usedIndex ):
                result += i + j
                usedIndex.add(i)
                usedIndex.add(j)
                break;
    print(result)

pairwise([1, 4, 2, 3, 0, 5], 7)