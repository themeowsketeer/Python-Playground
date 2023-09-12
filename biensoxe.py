n=int(input("nhap so luong bien xe: "))
bienso=[]
for i in range(n):
    bienso.append(int(input("nhap chuoi so: ")))
legal=[]
a=b=c=d=0
soluong=0
def calculate(x):
    a = x % 10
    b = (x // 10) % 10
    c = (x // 100) % 10
    d = (x // 1000) % 10
    tong = a+b+c+d
    return tong%10;
for i in range(0,len(bienso)):
    if calculate(bienso[i])==9:
        legal.append(bienso[i])
        soluong += 1
print("cac bien so xe la",legal)
print("so luong bien xe cho phep :",soluong)