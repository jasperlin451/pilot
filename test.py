#import excel file, print data
import studentImport
a = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
for i in range(len(a)):
    print(a[i].avail)

import importRooms
b=importRooms.scan('/home/jasper/pilot/rooms.xlsx')
for i in range(len(b)):
   print(b[i].day,b[i].time, b[i].classroom, b[i].group)
