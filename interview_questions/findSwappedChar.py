# Question: Given a string of length l, we can form a infinite long by moving the last character of the string
# to the front, then combining with the original string. Demonstrate:
# ABC -> ABCCAB - > ABCCABBABCCA -> ABCCABBABCCAAABCCABBABCC -> ABCCABBABCCAAABCCABBABCCCABCCABBABCCAAABCCABBABC
# Please find the k-th character of the string formed above.

# Brute force method -> does exactly like what the question inquires, feasibly coded, but not optimized
# Space complexity: O(k), since it is required to form a string of length longer than k-length in order to find k
# Time complexity: O(K), since it is required to iterate to whole length of the string and combine

def findChar_1(givenString, inquiredIndex):
    k = inquiredIndex
    while (len(givenString) < k):
        temp= givenString[len(givenString)-1] + givenString.replace(givenString[len(givenString)-1],'')
        givenString += temp
    return givenString[k-1]

# Optimized method -> a rule is found among the strings form:
# Check k = 22, l = 3 => x-length of final string is l*2*2*2 = 24 we have:
# ABCCABBABCCAAABCCABBABCC -> k-th char is B for x = 24
# However, check for x = 12:
# ABCCABBABCCA -> char B is at index 9 for x = 12
# Similarly, check for x = 6:
# ABCCAB -> char B is at index 2 for x = 6
# Doing some mathematics around:
# k = 22 / x = 12 -> k = k - x - 1 = 9
# k = 9 / x = 6 -> k = k - x - 1 = 2
# k = 2 / x = 3 = l -> Final location on the original l-length string: B
# Quick note:
# Check k = 19, l = 3 => x-length of final string is l*2*2*2 = 24 we have:
# ABCCABBABCCAAABCCABBABCC -> k-th char is B for x = 24
# Skip to doing some mathematics around:
# k = 20 / x = 12 -> k = k - x - 1 = 7
# k = 7 / x = 6 -> k = k - x - 1 = 0 (illogical since there exists no index 0 in mathematical list)
# If K = 0, grant K to be largest x as 2-multipling of l smaller than k
# Why? k = 1 is known as first letter of the new formed string before being combined -> last character
# of the string prior to combination
# Grant k = 6 since ( x = l*2 = 6 < k = 7) 
# k = 6 / x = 3 -> k = k - x - 1 = 2 -> Final location on the original l-length string: B
def findChar_2(s, k):
    l = len(s)
    while( l < k ):
        x = l
        while ((x*2) < k):
            x *= 2
        k = k - x - 1
        if (k == 0):
            k = x
    return s[k-1]

k = int(input())
s = input()
print(findChar_2(s,k))