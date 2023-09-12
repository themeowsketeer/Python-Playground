n=int(input("nhập số nguyên cho bài 1,2,3: "))
m=float(input("nhập số thực cho bài 4 và 6: "))
y=int(input("nhập số nguyên dương nhỏ cho bài 5 và 7: "))
x=float(input("nhập số thực cho bài 5 và 7: "))
bank=[]
for i in range(1,4):
    bank.append(float(input("nhập yêu cầu bài 8: ")))
def exercise1(n):
    S=round(3.14*n*n)
    P=round(3.14*n*2)
    answer={"S": S, "P": P}
    return answer
def exercise2(n):
    S=round(n/5*((n/5)*1.5))
    answer={"S": S}
    return answer
def exercise3(n):
    ten=n//10
    five=(n%10)//5
    two=(n%5)//2
    one=(n%5)%2
    portlist={'ten_coins': ten, 'five_coins': five, 'two_coins': two, 'one_coins': one}
    return portlist
def exercise4(n):
    y1="{:.2f}".format(n/3)
    y2="{:.2f}".format(n/7)
    answer={"y1": y1, "y2": y2}
    return answer
def exercise5(x,y):
    answer={"y": ((x**2+1)**y)}
    return answer
def exercise6(m):
    x="{:.4f}".format((m/3.14)**0.5)
    answer={"r": x}
    return answer
def exercise7(x,y):
    answer={"f(x)": (((x**2+x+1)**y)+((x**2-x+1)**y))}
    return answer
def exercise8(bank):
    money=bank[0]*((1+bank[2])**bank[1])
    answer={"total interest": "{:.0f}".format(money-bank[0])}
    return answer
print("Ket qua bai 1:",exercise1(n))
print("Ket qua bai 2:",exercise2(n))
print("Ket qua bai 3:",exercise3(n))
print("Ket qua bai 4:",exercise4(m))
print("Ket qua bai 5:",exercise5(x,y))
print("Ket qua bai 6:",exercise6(m))
print("Ket qua bai 7:",exercise7(n,m))
print("Ket qua bai 8:",exercise8(bank))