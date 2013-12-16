#scan in data file for student into people class
def scan(name,subject):
    import xlrd, person
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_name('Sheet1')
    num_rows = sheet.nrows
    num_cells = sheet.ncols
    data = []
    for curr_row in range(num_rows): #iterate through each row (student)
        temp1=[]
        avail=[] #time slots
        for curr_cell in range(num_cells):
            if (curr_cell > 3) and (curr_cell < num_cells-1): #group time slots together, the last row of data is preference so -1
                avail.append(sheet.cell_value(curr_row,curr_cell)) 
            else:		
                temp1.append(sheet.cell_value(curr_row,curr_cell))
        for a in range (len(temp1)):
            student = person.Person(temp1[0],temp1[1],temp1[2],temp1[3],subject,temp1[4],avail) #assign all the values to person class
        data.append(student) #add back to data
    return(data)
#first row of column is data labels, most interested in the time slots
