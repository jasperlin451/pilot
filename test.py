#import excel file, print data
import studentImport
a=studentImport.scan('/home/jasper/pilot/data.xls','Calc II')
for i in range(len(a)):
    print(a[i].jhu, a[i].name, a[i].mail, a[i].sub, a[i].avail)
