list=[]
count=0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                tong=a+b+c+d
                socuoicung=a*1000+b*100+c*10+d
                if tong % 10 == 9 and socuoicung >= 1000:
                    count += 1
                    list.append(socuoicung)
print("cac bien xe tong hop duoc: ",count)

