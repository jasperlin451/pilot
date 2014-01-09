#import excel file, print data
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
test=sort.Sorter(combos,['Calc II','Chem I'],rooms)
print(len(test))
for a in test[0]:
       print(a.classroom,a.subject,a.available)
