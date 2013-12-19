#import excel file, print data
import studentImport
a,b = studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
print (b)
import importRooms
b=importRooms.scan('/home/jasper/pilot/rooms.xlsx')
for i in range(len(b)):
    print(b[i].time, b[i].classroom, b[i].group)
