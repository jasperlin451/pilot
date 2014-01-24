import time
#import excel file, print data
starttime=time.time()
import studentImport
blah=[]
datas=[]
data,times = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
data2,times2 = studentImport.scan('/home/jasper/pilot/data2.xls','Chem I')
import importRooms
rooms,roomCount=importRooms.scan('/home/jasper/pilot/rooms.xlsx')
blah.append(times)
blah.append(times2)
datas.append(data)
datas.append(data2)
import combinations
combos=[]
combos.append(combinations.combinations(blah[0],8,data,roomCount))
combos.append(combinations.combinations(blah[1],10,data2,roomCount))
print(len(combos[0]))
print(len(combos[1]))

import sort
finalCombo,finalAssignments,finalWaitList=sort.Sorter(datas,combos,['Calc II','Chem I'],[8,10],rooms,blah)
print(len(finalCombo))
#determine which finalCombo fits the leader availability the best

#leaderData=leaderImport.scan()

#import assign

