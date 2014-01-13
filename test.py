import time
#import excel file, print data
starttime=time.time()
import studentImport
data,times = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
data2,times2 = studentImport.scan('/home/jasper/pilot/data2.xls','Chem I')
import importRooms
rooms,roomCount=importRooms.scan('/home/jasper/pilot/rooms.xlsx')

import combinations
combos=[]
combos.append(combinations.combinations(times,8,data,roomCount))
combos.append(combinations.combinations(times2,10,data2,roomCount))
print(len(combos[0]))
print(len(combos[1]))
#f=open('output','r+')
#for e in range(len(combos)):
#    f.write(str(combos[e])+'\n')
import sort
test=sort.Sorter(data,combos,['Calc II','Chem I'],[8,10],rooms)
print(len(test))
print(time.time()-starttime)
for i in test[0]:
    print(i.time,i.classroom,i.subject)
for b in test[1]:
    print(b.time,b.classroom,b.subject)
for a in rooms:
    print(a.time,a.classroom,a.subject)

