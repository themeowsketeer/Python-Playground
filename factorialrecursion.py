n=int(input())
def recursion(n):
    answer=[]
    if n>=1:
        answer.append(1)
    for i in range(1,n):
        answer.append(answer[i]+answer[i-2])
    print(answer)
recursion(n)