def scan(name):
    import xlrd, room
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_name('Sheet1')
    num_rows = sheet.nrows
    num_cells = sheet.ncols
    data = []
    for curr_row in range(num_rows-1): #skip first line
        temp=[]
        for curr_cell in range(num_cells):
            temp.append(sheet.cell_value(curr_row+1,curr_cell))
        data.append(room.Room(temp[0]+' '+temp[1],temp[2]))
    roomCount=roomCounter(data)
    return(data,roomCount)

def roomCounter(data):
    times=[]
    roomCount=[]
    for i in range(len(data)):
        times.append(data[i].time)
    temp=set(times)
    uniqueTimes=list(temp)
    for b in uniqueTimes:
        roomCount.append(times.count(b))
    return([uniqueTimes,roomCount])
