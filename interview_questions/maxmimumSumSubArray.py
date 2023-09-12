def max(num1, num2):
    if num1 > num2:
        return num1
    else: return num2

def n3solution(arr):
    best = 0
    for i in range(0,len(arr)):
        for b in range(i, len(arr)):
            sum = 0
            for c in range(i, b):
                sum += arr[c]
            best = max(best, sum)
    return best

def n2solution(arr):
    best = 0
    for a in range(0,len(arr)):
        sum = 0
        for b in range(a, len(arr)):
            sum += arr[b]
            best = max(best, sum)
    return best

def n1solution(arr):
    best = sum = 0
    for i in range(0,len(arr)):
        sum = max(arr[i], arr[i] + sum)
        best = max(best, sum)
    return best

# arr = [-1, 2, 4, -3, 5, 2, -5, 2]
# if ( (n1solution(arr) == n2solution(arr))
#     and (n2solution(arr) == n3solution(arr))
#     and (n1solution(arr) == n3solution(arr)) ):
#     print('True')
# else: print('False')
# n = int(input())
arr = list(map(int, input().split()))
print(f'{n1solution(arr)}')