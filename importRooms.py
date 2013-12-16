def scan(name):
    import xlrd, room
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_name('Sheet1')
    num_rows = sheet.nrows
    num_cells = sheet.ncols
    data = []
    for curr_row in range(num_rows):
        temp=[]
        for curr_cell in range(num_cells):
            temp.append(sheet.cell_value(curr_row,curr_cell))
        data.append(room.Room(temp[0],temp[1],temp[2]))
    return(data)
