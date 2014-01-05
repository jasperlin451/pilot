#import excel file, print data
import studentImport
data,times = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')

import importRooms
rooms,roomCount=importRooms.scan('/home/jasper/pilot/rooms.xlsx')

import combinations
combos=combinations.combinations(times,8,data,roomCount)
print(len(combos))
f=open('output','r+')
for e in range(len(combos)):
    f.write(str(combos[e])+'\n')

#import importRooms
#rooms=importRooms.scan('/home/jasper/pilot/rooms.xlsx')
#for i in range(len(rooms)):
#    print(rooms[i].time, rooms[i].classroom, rooms[i].group)
#import sort
#[c,d,e]=sort.checkRoom(rooms,'Monday 5 - 7 pm')
#print(c,d,e)
