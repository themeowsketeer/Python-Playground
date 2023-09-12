n=int(input("nhập n: "))
def recursion(n):
    answer=[]
    if n>=1:
        answer.append(1)
    if n>=2:
        answer.append(1)
    if n>=3:
        for i in range(2,n):
            answer.append(answer[i-1]+answer[i-2])
    print(answer)
recursion(n)