import datetime as d
import time as t
print(type(d))
print(dir(d))

'''
all kind of methods are present in python date

['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 
'timezone', 'tzinfo']

'''

print(d.datetime.now())  # printing the current date time

# for separate values
e=d.datetime.now()
print(e.year)
print(e.month)
print(e.day)
print(e.time())

print(e.strftime("%A"))

print("-------------------------")
dt=d.datetime(2023,10,10)
print(dt)
print(type(dt))


print("----------- using time --------------")
print(t.time())
print(t.localtime())  # time.struct_time(tm_year=2023, tm_mon=10, tm_mday=27, tm_hour=1, tm_min=5, tm_sec=46, tm_wday=4, tm_yday=300, tm_isdst=0)

print(t.asctime(t.localtime(t.time())))
