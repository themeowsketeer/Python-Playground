n=int(input("nhap so luong so: "))
lst=[]
even=[]
odd=[]
temp3=0
sapxep=[]
gay=[]
m=int
for i in range(n):
    lst.append(int(input("nhap chuoi so: ")))
gay=lst.copy()
for v in range(len(lst)):
    sapxep.insert(i,min(lst))
    lst.remove(min(lst))
print(sapxep)
for v in sapxep:
    if v % 2 == 0:
        even.append(v)
    else: odd.append(v)
tongchan=0
tongle=0
for u in even:
    tongchan += u
for u in odd:
    tongle += u
print("day so chan loc duoc la:",even," / so luong so chan co trong day:",len(even))
print("day so le loc duoc la:",odd," / so luong so le co trong day:",len(odd))
print("tong cua cac chu so chan trong day la:",tongchan)
print("tong cua cac chu so le trong day la:",tongle)