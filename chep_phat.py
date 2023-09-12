listtu=input("nhap list tu can chep phat: ")
chepphat=listtu.split(' ')
for j in chepphat:
    typical=[]
    for k in range(1,10):
        typical.append(j)
    print(typical)
    typical.clear