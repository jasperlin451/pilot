#import excel file, print data
import studentImport
a,b = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
#for i in range(len(a)):
#    print(a[i].avail)
#print(' ')

import importRooms
rooms=importRooms.scan('/home/jasper/pilot/rooms.xlsx')
for i in range(len(rooms)):
    print(rooms[i].time, rooms[i].classroom, rooms[i].group)
import sort
[c,d,e]=sort.checkRoom(rooms,'Monday 5 - 7 pm')
print(c,d,e)
