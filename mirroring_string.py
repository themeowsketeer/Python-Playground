word=input('type in a string: ')
def mirrorize(word):
    mirror=[]
    temp=[]
    for i in range(1,len(word)+1):
        temp.append(word[-1+1-i])
    print(temp)
    mirror.append(''.join(temp))
    return mirror
print(mirrorize(word))