#program to drop microseconds from datetime.


import datetime

x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S"))