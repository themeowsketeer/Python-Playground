def recursionDivision(n,resultList):
    if n == 1:
        resultList.append(1)
    else:
        resultList.append(n % 2)
        recursionDivision(n // 2,resultList)
def getBinaryResult(n):
    resultList=[]
    recursionDivision(n,resultList)
    resultList.reverse()
    return "".join(map(str, resultList))
def getDecimalResult(n):
    result=0
    for i in range(0,len(n)):
        if int(n[i])==1:
            result += pow(2,((len(n)-1)-i))
    return result
n = input("Type in a number: ")
nListOfString = ('').split(n)
number = ['0','1','2','3','4','5','6','7','8','9']
if (x not in number for x in nListOfString):
    print(f'You have input {n}: a binary number')
    print(f'The decimal form is: {getDecimalResult(n)}')
else:
    print(f'You have input {n}: a decimal number')
    print(f'The decimal form is: {getBinaryResult(int(n))}')