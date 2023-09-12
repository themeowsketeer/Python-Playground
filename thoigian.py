giay=int(input("nhap so giay: "))
ngay = gio = phut = 0
if giay>=86400:
    ngay = giay//86400
    giay %= 86400
    print(ngay, end = 'd / ')
if giay>= 3600:
    gio = giay // 3600
    giay %= 3600
    print(gio, end = 'h / ')
if giay>=60:
    phut = giay // 60
    giay %= 60
    print(phut, end = 'm / ')
if giay>0:
    print(giay, end = 's')