from datetime import datetime
from datetime import date

def setTime(dateBegin,dateEnd,day):
    day1 = 0
    date = []
    while dateBegin  <= dateEnd:
        dateBegin = dateBegin + day1
        time = datetime.fromtimestamp(dateBegin)
        wd = datetime.weekday(time)
        days = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ Nhật']
        checkdays = days[wd]
        if (checkdays == day):
            date.append(dateBegin)
        else:
            pass
        day1 = 86400.0
        # print(dates)
    return date


    # hàm chuyển sang timestamp
def ConvertTimestamp(year,month,day):
    date = datetime(year,month,day)
    dateBegin = datetime.timestamp(date)
    return dateBegin


# hàm cắt date
def cutdate(date):
    a = date.split("/")
    b = []
    for i in a:
        b.append(int(i))
    return b
# ConvertTimestamp(2020,11,27)
# ConvertTimestamp(2020,12,5)
print(setTime(ConvertTimestamp(2020,11,27),ConvertTimestamp(2020,12,15),"Thứ 2"))

