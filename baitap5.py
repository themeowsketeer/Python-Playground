n=int(input("nhap chu so n: "))
j=0
tong=0
reversed=[]
while n!= 10 and n % 10 != 0:
    j = n % 10
    reversed.append(j)
    tong += j
    n //= 10
tonggay=0
for i in range(0,len(reversed)):
    tonggay += reversed[i]
print(n)
print(tong)
print(reversed)
print(tonggay)