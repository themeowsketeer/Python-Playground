day=int(input("Enter a day: "))
month=int(input("Enter a month: "))
year=int(input("Enter a year: "))
def leapyear(year):
    if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0 ):
        return True
    else: return False
while (day < 0 and month < 0) or \
    (day > 29 and month == 2 and leapyear(year)==1) or \
        (day >= 29 and month ==2 and leapyear(year)==0) or \
            (month > 7 and month % 2 == 1 and day >= 31) or \
                (month <= 7 and month % 2 == 1 and day > 31) or \
                    (month % 2 == 0 and month >= 7 and day > 31) or \
                        (month < 7 and month % 2 == 0 and day >= 31):
    print('Bạn đã nhập ngày sai. Xin mời nhập lại')
    day=int(input("Enter a day: "))
    month=int(input("Enter a month: "))
    year=int(input("Enter a year: ")) 
def calendarcal(day,month,year):
    sum=0
    calendarday=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 1:
        sum = day
    else:
        for i in range(1,len(calendarday)):
            if i < month:
                sum += calendarday[i]
        if leapyear(year):
            sum += 1
            sum += day
        else: sum += day
    return sum
print(f"Total days up to input date is: {calendarcal(day,month,year)}")