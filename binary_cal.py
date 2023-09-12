n = input("Type in a binary number: ")
result=0
for i in range(0,len(n)):
    if int(n[i])==1:
        result += pow(2,((len(n)-1)-i))
print("The decimal is",result)