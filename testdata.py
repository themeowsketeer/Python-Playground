#[ vị trí bắt đầu : vị trí kết thúc : bước nhảy]
#đoạn [::-1] tương đương nghĩa là lấy toàn bộ các phần tử (bỏ trống 2 số đầu) nhưng theo bước nhảy là từ -1 
#(1 là mặc định như bình thường) thì theo chiều ngược lại.
#[a , b, c, d][::-1] == [d, c, b, a]
#a <- b <- c <- d (1 bước theo chiều âm)
#tác dụng tương tự như reversed()
#ví dụ với [::-2]
#[a, b, c, d][::-2] == [d, b]
#b < -- d (2 bước theo chiều âm)
s = input()
print(" ".join(s.split(" ")[::-1]))