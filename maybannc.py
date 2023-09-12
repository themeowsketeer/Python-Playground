traxanhc2=9000
sting=11000
pepsi=10000
warrior=13000
ncsuoi=5000
charge=0
list=["traxanhc2","sting","pepsi","warrior","ncsuoi"]
tienvao=int(input("nhap so tien vao: "))
print(list)
nuocdcchon=input("nhap ten nuoc ban muon mua: ")
if nuocdcchon == list[0]:
    charge=tienvao-traxanhc2
elif nuocdcchon == list[1]:
    charge=tienvao-sting
elif nuocdcchon == list[2]:
    charge=tienvao-pepsi
elif nuocdcchon == list[3]:
    charge=tienvao-warrior
elif nuocdcchon == list[4]:
    charge=tienvao-ncsuoi
else: print("xin hay thoat ra va nhap lai")
while nuocdcchon in list:
    if charge >= 0:
        print("Mua hang thanh cong. So tien con lai ban co la", charge)
    else: print("Ban khong du tien de mua thuc uong nay")
    break
