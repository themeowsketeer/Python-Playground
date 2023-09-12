lst=[x for x in input("chuoi so ban nhap vao. Nhap enter khi ban da nhap xong: ").split(", ")]
min=lst[0]
vitri1=1
vitri2=1
max=lst[0]
for i in range(1,len(lst)):
    if lst[i]<min:
        min=lst[i]
        i += 1
        vitri1=i
    if lst[i]>max:
        max=lst[i]
        i += 1
        vitri2=i
print("chuoi so duoc nhap vao: ",lst)
print("so nho nhat: ",min)
print("vi tri so nho nhat: ",vitri1)
print("so lon nhat: ",max)
print("vi tri so lon nhat: ",vitri2)