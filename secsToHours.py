from datetime import timedelta

inp = int(input("Input the number of seconds: "))
time = str(timedelta(seconds=inp))

hr = inp//60**2
print(hr)
time = str(hr) + time[time.index(":"):]
if len(time) < 8:
    time = "0" + time
    
print(time)