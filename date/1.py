#subtracting 5 days from the currebt date

import datetime

x = datetime.datetime.now()
c = int(x.strftime("%d"))
print (c -1)   