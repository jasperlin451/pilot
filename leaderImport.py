def scan(filename):
    import xlrd, leader
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name('leaders')
    num_rows = sheet.nrows
    num_cells = sheet.ncols
    data = []
    times = []
    subjects=[]
    timeslots=26 #can be changed
    for curr_row in range(num_rows):
        available=[]
        subjectPreference=[]
        for i in range(timeslots):
            if curr_row<1:
            #start at 3rd column
                times.append(sheet.cell_value(0,i+2))
            else:
                if sheet.cell_value(curr_row,i+2)==1:
                    available.append(sheet.cell_value(0,i+2))
                else:
                    available.append(' ')
        for j in range(num_cells-timeslots-2):
            if curr_row<1:
                subjects.append(sheet.cell_value(0,j+timeslots+2))
            else:
                subjectPreference.append(int(sheet.cell_value(curr_row,j+timeslots+2)))
        if curr_row !=0:
            first=sheet.cell_value(curr_row,0)
            last=sheet.cell_value(curr_row,1)
            data.append(leader.Leader(first,last,subjectPreference,available))
    return(times,subjects,data)            
