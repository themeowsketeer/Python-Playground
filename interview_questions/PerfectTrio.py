# Question: Given a n-length array A of negative and positive numbers,
# please find the biggest multiplication of a sub array of 3 number.
# Constraint: |A[i]| < 1000
## Two different strategies for 2 different types of input. Please comment out one if the other is intended to be tested

def max(num1, num2):
    if num1 > num2:
        return num1
    else: return num2

# # Strategy that involve input elements of the array by hand
# n = int(input()) # input array length
# min1 = min2 = 1001
# max1 = max2 = max3 = -1001
# while (n > 0):
#     x = int(input()) # Array's element
#     if (x > max1):
#         max3 = max2
#         max2 = max1
#         max1 = x
#     elif (x > max2):
#         max3 = max2
#         max2 = x
#     elif (x > max3):
#         max3 = x
#     if (x < min1):
#         min2 = min1
#         min1 = x
#     elif (x < min2):
#         min2 = x
#     n -= 1
# print(f'{ max( (max1*max2*max3),(min1*min2*max1) ) }')

## Strategy that involve input array as a whole list
# n = int(input()) # input array length
# min1 = min2 = 1001
# max1 = max2 = max3 = -1001
# A = list(map(int, input().split()))
# while (len(A) != n):
#     print('Length of array A is different from n. Please re-type')
#     A = list(map(int, input().split()))
# for i in range(0,n):
#     if (A[i] > max1):
#         max3 = max2
#         max2 = max1
#         max1 = A[i]
#     elif (A[i] > max2):
#         max3 = max2
#         max2 = A[i]
#     elif (A[i] > max3):
#         max3 = A[i]
#     if (A[i] < min1):
#         min2 = min1
#         min1 = A[i]
#     elif (A[i] < min2):
#         min2 = A[i]
# print(f'{ max( (max1*max2*max3),(min1*min2*max1) ) }')

# Submitted code with 0.84s total run time and 11.2MB used for 40 cases

n = int(input())
min1 = min2 = 100001
max1 = max2 = max3 = -100001
# A = [int(x) for x in input().split()]
A = list(map(int, input().split()))
for i in range(0,n):
    if (A[i] > max1):
        max3 = max2
        max2 = max1
        max1 = A[i]
    elif (A[i] > max2):
        max3 = max2
        max2 = A[i]
    elif (A[i] > max3):
        max3 = A[i]
    if (A[i] < min1):
        min2 = min1
        min1 = A[i]
    elif (A[i] < min2):
        min2 = A[i]
print(f'{ max( (max1*max2*max3),(min1*min2*max1) ) }')
